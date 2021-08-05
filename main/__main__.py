# __main__.py
"""
    vulDetect: command line tool scanning GitHub repositories for vulnerabilities and producing graph visualizations.
"""
import argparse, os, json
from main.helper import Helper


def _load_config():
    """
    Load token from config.json

    :return: True, Token or False, None
    """
    file = os.getcwd() + '/config.json'

    try:
        if os.path.isfile(file):
            with open(file) as json_file:
                config = json.load(json_file)
                return True, config['token']
        else:
            return False, None
    except Exception as e:
        return False, None


def operate(helper, users, repos, write, show, switch='all'):
    """
    Uses helper class to operate graph generation methods

    :param helper: input helper object
    :param users: input user object
    :param repos: input repo object
    :param write: input boolean value on file write
    :param show: input boolean value on show
    :param switch: input string to identify which function to handle
    """
    h = helper  # To not have to type out helper

    if switch == 'user' or switch == 'all':
        h.gen_user_graph(users, show=show, write=write)
    if switch == 'repo' or switch == 'all':
        h.gen_repo_graph(repos, show=show, write=write)
    if switch == 'bip' or switch == 'all':
        h.gen_bipartite_graph(users, repos, show=show, write=write)
    if switch == 'clustu' or switch == 'all':
        h.gen_clusterings(h.gen_user_graph(users, show=False, write=False), show=show, write=write)
    if switch == 'clustr' or switch == 'all':
        h.gen_clusterings(h.gen_repo_graph(repos, show=False, write=False), show=show, write=write)


def main():
    # TODO: Cleanup arguments/add functionality
    # TODO: Add setup.cfg when completed
    boolean, token = _load_config()  # Load token from config file, if exists

    parser = argparse.ArgumentParser(prog='vulDetect',
                                     description='vulDetect - a GitHub vulnerability visualization tool',
                                     epilog='Clusterings will not work with only one repo')
    if boolean:
        print('TOKEN LOADED THROUGH CONFIG')
    else:
        parser.add_argument('token', metavar='TOKEN', type=str)
    parser.add_argument('-q', '--query', metavar=('QUERY', 'NUMBER'), dest='query', nargs=2,
                        default=['language:python', 10],
                        help='Query repos based on input: {Query String}, {Number of Repos}')
    parser.add_argument('-w', '--write', dest='write', default=False, action='store_true',
                        help='Write graph results to file.')
    parser.add_argument('-s', '--show', dest='show', default=False, action='store_true',
                        help='Show graph results in interactive window')
    parser.add_argument('-b', '--bipartite', dest='bip', default=False, action='store_true',
                        help='Produce bipartite graph output')
    parser.add_argument('-u', '--user', dest='usr', default=False, action='store_true',
                        help='Produce user graph output')
    parser.add_argument('-r', '--repo', dest='repo', default=False, action='store_true',
                        help='Produce repo graph output')
    parser.add_argument('-cu', '--usercluster', dest='clustu', default=False, action='store_true',
                        help='Produce cluster based on user graph')
    parser.add_argument('-cr', '--repocluster', dest='clustr', default=False, action='store_true',
                        help='Produce cluster based on repo graph')

    args = parser.parse_args()  # Parse arguments to object
    if not boolean:  # If no config file loaded, set user input
        token = args.token

    # Instantiate helper object
    h = Helper(token)

    # Handle arguments
    if args.query:
        # TODO: Could use ability to disable some scans, in future
        print('Processing query...')
        repos, users = h.process_urls(h.return_query_list(str(args.query[0]), int(args.query[1])))
        print('Processing finished.')
    if args.show:  # Handle show arguments
        if args.bip:
            operate(h, users, repos, False, args.show, 'bip')
        if args.usr:
            operate(h, users, repos, False, args.show, 'user')
        if args.repo:
            operate(h, users, repos, False, args.show, 'repo')
        if args.clustu:
            operate(h, users, repos, False, args.show, 'clustu')
        if args.clustr:
            operate(h, users, repos, False, args.show, 'clustr')
        if not args.bip and not args.usr and not args.repo and not args.clustu and not args.clustr:
            operate(h, users, repos, False, args.show)
    if args.write:  # Handle write arguments
        if args.bip:
            operate(h, users, repos, args.write, False, 'bip')
        if args.usr:
            operate(h, users, repos, args.write, False, 'user')
        if args.repo:
            operate(h, users, repos, args.write, False, 'repo')
        if args.clustu:
            operate(h, users, repos, args.write, False, 'clustu')
        if args.clustr:
            operate(h, users, repos, args.write, False, 'clustr')
        if not args.bip and not args.usr and not args.repo and not args.clustu and not args.clustr:
            operate(h, users, repos, args.write, False)


if __name__ == '__main__':
    main()
