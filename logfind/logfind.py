__author__ = 'deonheyns'
import os
import glob
import re

class Logfind(object):
    def __init__(self):
        self.__dot_logfind = '.logfind'

    # method to read .logfind to obtain the log files that are important
    # presume .logfind will be in ~ also try logfind folder then executing folder
    def read_dot_logfind(self):
        important_files = []
        errors = []
        try:
            important_files.append(self.__read_dot_logfind_from_home_directory())
        except IOError as ex:
            errors.append(ex)

        try:
            important_files.append(self.__read_dot_logfind_from_logfind_directory())
        except IOError as ex:
            errors.append(ex)

        try:
            important_files.append(self.__read_dot_logfind_from_executing_directory())
        except IOError as ex:
            errors.append(ex)

        if len(important_files) == 0 and len(errors) > 0:
            raise Exception(errors)

        important_files = self.__flatten(important_files)
        important_files = [l.rstrip() for l in important_files]  # Chomp
        return important_files

    # method to scan current directory for all files that match the .logfind criteria
    @staticmethod
    def get_log_files(logs_patterns):
        results = []
        executing_directory = os.getcwd()

        combined = '(' + ')|('.join(logs_patterns) + ')'
        for f in os.listdir(executing_directory):
            if re.search(combined, f, re.I):
                    results.append(f)

        return results

    # read the passed in logfiles and find the passed in value
    def read_log_files(self, log_files, text, treat_as_or=False):
        results = []
        regex = self.__create_regex_pattern(text, treat_as_or)
        for log_file in log_files:
            with file(log_file, "r") as f:
                contents = f.read()
                search = re.search(regex, contents, re.M | re.I)
                if search:
                    results.append(log_file)
        return results

    def __read_dot_logfind_from_home_directory(self):
        home_directory = os.environ['HOME']
        directory = os.path.join(home_directory, self.__dot_logfind)
        with file(directory, "r") as f:
            return f.readlines()

    def __read_dot_logfind_from_logfind_directory(self):
        logfind_directory = os.path.dirname(os.path.realpath(__file__))
        directory = os.path.join(logfind_directory, self.__dot_logfind)
        with file(directory) as f:
            return f.readlines()

    def __read_dot_logfind_from_executing_directory(self):
        executing_directory = os.getcwd()
        directory = os.path.join(executing_directory, self.__dot_logfind)
        with file(directory) as f:
            return f.readlines()

    def __create_regex_pattern(self, text, treat_as_or=False):
        if not treat_as_or:
            regex = r'(?=.*?\b{0}\b.*?)'
            pattern = ''.join([regex.format(x) for x in text.split()])
            return pattern

        else:
            regex = r'(?=.*?\b{0}\b.*?)'
            pattern = '|'.join([regex.format(x) for x in text.split()])
            return pattern

    @staticmethod
    def __flatten(items):
        flatten = [item for sublist in items for item in sublist]
        return flatten