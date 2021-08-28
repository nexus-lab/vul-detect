# vulDetect
vulDetect is a command line tool that utilizes multiple open source scanners to scan GitHub repositories for secrets and vulneralbilites and visualizes the results in a graph structure. 

## Features
- Usage of GitHub API to query a number of repositories
- Static code analysis using [flawfinder](https://github.com/david-a-wheeler/flawfinder) and [bandit](https://github.com/PyCQA/bandit)
- Secret scanning using [gitleaks](https://github.com/zricethezav/gitleaks)
- Bipartite graph output showing user to repository relationship
- User graph output showing shared vulnerabilities among users
- Repo graph output showing shared vulnerabilities among repos
- .GEXF and .PNG outputs
- Utilization of DeepWalk algorithm to show latent relationships between users and between repositories

## Installation
vulDetect relies on several tools that are both either in PyPi or not. Compatibility with multiple systems is limited at this time. 
### Linux
```bash
make all
```
### Windows
```bash
# NOTE: As of now, you will have to install the gitleaks binary (gitleaks.exe) manually by adding it to your PATH until an install script is made. See gitleaks GitHub.

python -m build
pip install dist/vulDetect-0.5.tar.gz
```

## Usage
```bash
usage: vulDetect [-h] [-q QUERY NUMBER] [-w] [-s] [-b] [-u] [-r] [-cu] [-cr] TOKEN

vulDetect - a GitHub vulnerability visualization tool

positional arguments:
  TOKEN                 GitHub API Token

optional arguments:
  -h, --help            show this help message and exit
  -q QUERY NUMBER, --query QUERY NUMBER
                        Query repos based on input: {Query String}, {Number of Repos}
  -w, --write           Write graph results to file.
  -s, --show            Show graph results in interactive window
  -b, --bipartite       Produce bipartite graph output
  -u, --user            Produce user graph output
  -r, --repo            Produce repo graph output
  -cu, --usercluster    Produce cluster based on user graph
  -cr, --repocluster    Produce cluster based on repo graph

Clusterings will not work with only one repo
```

## Configuration
vulDetect has the ability to load your api token through a json file named `config.json`. In your working directory, simply add the file with the format as follows:
```json
{"token": "your token here"}
```
If you do not know where to aquire a token, consult the GitHub documentation on [personal access tokens](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token).

## Sample Case
___
Provided a valid api token, vulDetect has the ability to scan repos based on an input query. See the [GitHub Search Documentation](https://docs.github.com/en/rest/reference/search) for more information.

The command below will query GitHub for 10 repos from the organization Facebook and output the user graph associated with those repos provided a `config.json`: 
```bash
vulDetect -q org:facebook 10 -u -s
```
Note that this may take some time. Additionally, you cannot access private organizations unless your api token or account has access to said organization. This does mean, however, that you have the ability to query any publicly available organization or repo if it fits the api search criteria.

Below is an example of querying for 10 repos under the query `language:python`:
```bash
vulDetect -q language:python 10 -cr -w
```
This will scan the top 10 python repos and produce the clusterings for repos to a file named `cluster.png`. The results can be interpreted to show which vulnerabilities are the most common among the ten python repos and which repos contributed to those vulnerabilities, likewise for users if `-cu` is specified. Notice the distance between nodes represents the similarity in relationship between any two repos. This can be representative of common vulnerabilities, common users with the same vulnerabilities, etc. (NOTE that names are not included in the output. *yet) 

By default, vulDetect will show all graphs and outputs, but will not write any file unless you specify the `-w` argument. If you wish to do both, specify both `-w` and `-s`. vulDetect also does not have the ability to specify an output path (yet). vulDetect will (as of now) write all output files to the current working directory. See the laundry list at the bottom of this file for future prospective changes.  
___

## Credits and Information
- Info on DeepWalk: http://perozzi.net/publications/14_kdd_deepwalk.pdf  
- Flawfinder: https://github.com/david-a-wheeler/flawfinder 
- Bandit: https://github.com/PyCQA/bandit
- Gitleaks: https://github.com/zricethezav/gitleaks 
- Inspiration for this project: http://sagarsamtani.com/wp-content/uploads/2020/11/Lazarine-et-al.-2020-ISI.pdf 

## Laundrylist
- Metadata identifying users/repos and vulnerabilities to program outputs. (Both networkx and .gexf)
- ~~Names added to clustering output.~~
- Ability to output file containing names and vulnerabilities associated with name. (Both user and repo)
- Additional CLI options specifying output path, scanner usage, graph size, and attributes for graphs and clusters.
- Addition of some prospective scanners such as VisualCodeGrepper, RIPS, and Brakeman.
- Optimizations minimizing runtime and managing disk usage.
- Cleanup of program output to a more useful and readable format. 
- Possible dynamic scan implementation.

