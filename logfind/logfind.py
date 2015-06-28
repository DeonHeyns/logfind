__author__ = 'deonheyns'
import os
import re


class Logfind(object):
    def __init__(self):
        self.__dot_logfind = '.logfind'

    def find(self, text, treat_as_or=False):
        patterns = self.read_dot_logfind()
        log_files = self.get_log_files(patterns)
        matches = self.read_log_files(log_files, text, treat_as_or=treat_as_or)
        return matches

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
            raise Exception('No .logfind file found in user, logfind or current directory.')

        important_files = set(self.__flatten(important_files))
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
            with open(log_file, 'r') as f:  # Buffered read
                for line in f:
                    search = re.search(regex, line, re.M | re.I)
                    if search:
                        results.append(log_file)
                        break
        return results

    def __read_dot_logfind_from_home_directory(self):
        home_directory = os.environ['HOME']
        directory = os.path.join(home_directory, self.__dot_logfind)
        with file(directory, 'r') as f:
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
        text = text.split()
        regexes = []
        left_overs = []
        for t in text:
            if self.__is_regex(t):
                regexes.append(t)
            else:
                left_overs.append(t)

        text = left_overs
        patterns = []
        if not treat_as_or:
            regex = r'(?=.*?\b{0}\b.*?)'
            patterns.extend([regex.format(x) for x in text])
            patterns.extend(['({})'.format(x) for x in regexes])
            pattern = ''.join(patterns)
            return pattern

        else:
            regex = r'(?=.*?\b{0}\b.*?)'
            patterns.extend([regex.format(x) for x in text])
            patterns.extend([x for x in regexes])
            pattern = '|'.join(patterns)
            return pattern

    @staticmethod
    def __is_regex(pattern):
        match = re.match(r'^[a-zA-Z0-9]*$', pattern)
        if match:
            return False

        try:
            re.compile(pattern)
        except Exception:
            return False
        return True

    @staticmethod
    def __flatten(items):
        flatten = [item for sublist in items for item in sublist]
        return flatten
