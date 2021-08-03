# __main__.py
"""
    vulDetect: command line tool scanning GitHub repositories for vulnerabilities and producing graph visualizations.
"""
# TODO: Add documentation
import argparse, os, json
from main.helper import Helper


def _load_config():
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


def operate(helper, users, repos, write, show):
    h = helper

    user_graph = h.gen_user_graph(users, show=show, write=write)
    repo_graph = h.gen_repo_graph(repos, show=show, write=write)
    h.gen_bipartite_graph(users, repos, show=show, write=write)
    h.gen_clusterings(user_graph, show=show, write=write)
    h.gen_clustering(repo_graph, show=show, write=write)


def main():
    # TODO: Formulate arguments and implement
    # TODO: Add setup.cfg when completed
    boolean, token = _load_config()

    parser = argparse.ArgumentParser(prog='vulDetect',
                                     description='vulDetect - a GitHub vulnerability visualization tool')
    if boolean:
        print('TOKEN LOADED THROUGH CONFIG')
    else:
        parser.add_argument('token', metavar='TOKEN', dest='token', type=str)
    parser.add_argument('-q', '--query', metavar=('QUERY', 'NUMBER'), dest='query', nargs=2,
                        default=['language:python', 10],
                        help='Query repos based on input: {Query String}, {Number of Repos}')
    parser.add_argument('-w', '--write', dest='write', default=True, action='store_true')
    parser.add_argument('-s', '--show', dest='show', default=False, action='store_true')

    args = parser.parse_args()
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
    if args.write:
        operate(h, users, repos, args.write, False)
    if args.show:
        operate(h, users, repos, False, args.show)


if __name__ == '__main__':
    main()
