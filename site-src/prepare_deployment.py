"""
This script aims to build a local list of all compiled files and compare it with the already published files in order to produce a final list to upload.

The latest compiled file list will also be uploaded in order to have a single file reference at the remote storage location that can be retrieved easily in a single call.

The intent is to use this script with file from a local filesystem that need to be synchronized with an S3 bucket.
"""

import traceback
import os
import argparse
import logging
import hashlib
import boto3
import tempfile


###############################################################################
###                                                                         ###
###                   C O M M A N D    L I N E    A R G S                   ###
###                                                                         ###
###############################################################################


def get_argument_string(arg_data)->str:
    if isinstance(arg_data, str):
        return arg_data
    elif isinstance(arg_data, list):
        return arg_data[0]
    return ''


parser = argparse.ArgumentParser(description='Prepare a list of files that are new/changed to upload to AWS S3')
parser.add_argument(
    '--no-debug', 
    dest='debug',
    action='store_false',
    default=False,
    help='Disable debug logging (this is the default)'
)
parser.add_argument(
    '--debug', 
    dest='debug',
    action='store_true',
    help='Enable debug logging'
)
parser.add_argument(
    '--directory', 
    dest='directory',
    default='{}{}site'.format(os.getcwd(), os.sep),
    nargs=1,
    type=str,
    metavar='DIR',
    help='The directory containing the files to compare againsty the remote files'
)
parser.add_argument(
    '--bucket-name', 
    dest='bucket_name',
    nargs=1,
    type=str,
    metavar='S3_BUCKET_NAME',
    required=True,
    help='The S3 Bucket Name'
)
parser.add_argument(
    '--aws-region', 
    dest='aws_region',
    nargs=1,
    type=str,
    metavar='AWS_REGION',
    required=False,
    default='us-east-1',
    help='The S3 Bucket Name'
)
args = parser.parse_args()


AWS_REGION = get_argument_string(arg_data=args.aws_region).lower()


###############################################################################
###                                                                         ###
###                              L O G G I N G                              ###
###                                                                         ###
###############################################################################


final_debug_level = logging.INFO
if args.debug is True:
    final_debug_level = logging.DEBUG

logger = logging.getLogger('spam_application')
logger.setLevel(final_debug_level)
ch = logging.StreamHandler()
ch.setLevel(final_debug_level)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

logger.info('Starting')
logger.debug('DEBUG enabled')


###############################################################################
###                                                                         ###
###                            F U N C T I O N S                            ###
###                                                                         ###
###############################################################################


def get_all_files(directory: str)->dict:
    file_data = dict()
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = '{}{}{}'.format(root, os.sep, file)
            checksum = hashlib.md5(open(file_path,'rb').read()).hexdigest()
            logger.debug('{} {}'.format(checksum, file_path))
            file_data[file_path] = checksum
    return file_data


def generate_manifest_from_files(files: dict, directory: str)->str:
    manifest = ''
    for file, file_checksum in files.items():
        final_file = file.replace(directory, '')
        if final_file.startswith(os.sep) is True:
            final_file = final_file.replace(os.sep, '', 1)
        manifest = '{}{} {}\n'.format(manifest, file_checksum, final_file)
    logger.debug('manifest contains {} bytes'.format(len(manifest)))
    return manifest


def generate_files_from_manifest(manifest: str)->dict:
    files = dict()
    if manifest is not None:
        if len(manifest) > 0:
            for line in manifest.split('\n'):
                logger.debug('Processing line: {}'.format(line))
                if len(line) > 0:
                    checksum, file = line.split(' ')
                    files[file] = checksum
    logger.debug('Extracted {} files'.format(len(files)))
    return files 


def generate_list_of_files_to_upload(
    local_manifest: str,    # Lines containing something like "c6e9fb78d6ab9c56c558b72b73e29522 blog/2022/2022-02-24.html" on each line
    remote_manifest: str,   # Lines containing something like "67e41450ce5bb8567efdc606f3e424c8 blog/2022/2022-02-24.html" on each line
    directory: str
)->dict:
    uploads = dict()    # INDEX=local file name    DATA: key name
    remote_manifest_data = generate_files_from_manifest(manifest=remote_manifest)   # { 'blog/2022/2022-02-24.html': '67e41450ce5bb8567efdc606f3e424c8', .... }
    for local_filename, local_checksum in generate_files_from_manifest(manifest=local_manifest).items():    # { 'blog/2022/2022-02-24.html': 'c6e9fb78d6ab9c56c558b72b73e29522', .... }
        if local_filename not in remote_manifest_data:
            local_file_path = '{}{}{}'.format(
                directory,
                os.sep,
                local_filename
            )
            uploads[local_file_path] = local_filename
        else:
            if local_checksum != remote_manifest_data[local_filename]:
                uploads[local_file_path] = local_filename
    logger.debug('uploads={}'.format(uploads))
    return uploads


###############################################################################
###                                                                         ###
###                        A W S    F U N C T I O N S                       ###
###                                                                         ###
###############################################################################


AWS_REGION = os.getenv('AWS_REGION', 'eu-central-1')


def get_aws_client(boto3_library, service: str='s3', region: str=AWS_REGION):
    return boto3_library.client(service_name=service, region_name=region)


def get_aws_resource(boto3_library, service: str='s3', region: str=AWS_REGION):
    return boto3_library.resource(service_name=service, region_name=region)


def retrieve_manifest_from_s3(
    bucket_name: str, 
    manifest_filename: str='INVENTORY',
    target_directory: str=tempfile.gettempdir(), 
    client=get_aws_resource(boto3_library=boto3,service='s3')
)->str:
    target_path = '{}{}{}'.format(
        target_directory,
        os.sep,
        manifest_filename
    )
    data = None
    try:
        client.meta.client.download_file(
            Bucket=bucket_name, 
            Key=manifest_filename, 
            Filename=target_path
        )
        with open(target_path, 'r') as f:
            data = f.read()
        if len(data) == 0:
            data = None
    except:
        logger.info('Unable to retrieve "{}" from "{}" - enable debug to see full stacktrace'.format(manifest_filename, bucket_name))
        logger.debug('EXCEPTION: {}'.format(traceback.format_exc()))
    return data


###############################################################################
###                                                                         ###
###                                 M A I N                                 ###
###                                                                         ###
###############################################################################


def main():
    directory = get_argument_string(arg_data=args.directory)
    logger.info('Scanning directory {}'.format(directory))
    files = get_all_files(directory=directory)
    logger.info('Scanned {} local files'.format(len(files)))
    local_manifest = generate_manifest_from_files(files=files, directory=directory)
    remote_manifest = retrieve_manifest_from_s3(
        bucket_name=get_argument_string(arg_data=args.bucket_name).lower()
    )
    files_to_upload = generate_list_of_files_to_upload(
        local_manifest=local_manifest,
        remote_manifest=remote_manifest,
        directory=directory
    )
    # TODO Generate list of remote files to DELETE
    # TODO Upload local files to remote
    # TODO Delete remote files no longer locally present


if __name__ == '__main__':
    main()

