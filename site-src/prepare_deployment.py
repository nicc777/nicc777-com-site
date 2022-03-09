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


###############################################################################
###                                                                         ###
###                   C O M M A N D    L I N E    A R G S                   ###
###                                                                         ###
###############################################################################


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
args = parser.parse_args()


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


def get_argument_string(arg_data)->str:
    if isinstance(arg_data, str):
        return arg_data
    elif isinstance(arg_data, list):
        return arg_data[0]
    return ''


def get_all_files(directory: str)->dict:
    file_data = dict()
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = '{}{}{}'.format(root, os.sep, file)
            checksum = hashlib.md5(open(file_path,'rb').read()).hexdigest()
            logger.debug('{} {}'.format(checksum, file_path))
            file_data[file_path] = checksum
    return file_data


def generate_manifest_from_files(files: dict)->str:
    manifest = ''
    for file, file_checksum in files.items():
        manifest = '{}{} {}\n'.format(manifest, file_checksum, file)
    logger.debug('manifest contains {} bytes'.format(len(manifest)))
    return manifest


def generate_files_from_manifest(manifest: str)->dict:
    files = dict()
    if len(manifest) > 0:
        for line in manifest.split('\n'):
            logger.debug('Processing line: {}'.format(line))
            if len(line) > 0:
                checksum, file = line.split(' ')
                files[file] = checksum
    logger.debug('Extracted {} files'.format(len(files)))
    return files


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
    local_manifest = generate_manifest_from_files(files=files)

    test = generate_files_from_manifest(manifest=local_manifest)


if __name__ == '__main__':
    main()

