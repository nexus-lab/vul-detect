#__main__.py
"""
    vulDetect: command line tool scanning GitHub repositories for vulnerabilities and producing graph visualizations.
"""
import argparse
import helper


def _load_config():
    # TODO: Add ability to load token etc through file
    pass


def main():
    # TODO: Formulate arguments and implement
    # TODO: Add setup.cfg when completed
    parser = argparse.ArgumentParser(prog='vulDetect',
                                     description='vulDetect - a GitHub vulnerability visualization tool')
    parser.add_argument('token', type=str, dest='token')
    parser.add_argument('-l', '--load', dest='load_status')
    parser.add_argument('-q', '--query', 'number', dest='query', help='Query results based on ')
    parser.add_argument('-w', '--write', dest='write')
    parser.add_argument('-s', '--show', dest='show')

    args = parser.parse_args()

    # TODO: Do stuff with the args


if __name__ == '__main__':
    main()
