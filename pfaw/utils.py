from datetime import datetime


def convert_iso_time(isotime):
    """Will convert an isotime (string) to datetime.datetime"""
    return datetime.strptime(isotime, '%Y-%m-%dT%H:%M:%S.%fZ')
