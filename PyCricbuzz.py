from pycricbuzz import Cricbuzz
import json


def match_info(mid):
    c = Cricbuzz()
    info = c.matchinfo(mid)
    print(json.dumps(info, indent=4, sort_keys=True))


def live_score(mid):
    c = Cricbuzz()
    lscore = c.livescore(mid)
    print(json.dumps(lscore, indent=4, sort_keys=True))


def commentary(mid):
    c = Cricbuzz()
    comm = c.commentary(mid)
    print(json.dumps(comm, indent=4, sort_keys=True))


def scorecard(mid):
    c = Cricbuzz()
    scard = c.scorecard(mid)
    print(json.dumps(scard, indent=4, sort_keys=True))


def current_match_status():
    c = Cricbuzz()
    matches = c.matches()
    return matches[0]["status"]


if __name__ == '__main__':
    # c = Cricbuzz()
    # matches = c.matches()
    # print(type(matches))
    # print(json.dumps(matches[0], indent=4))
    # match_id = matches[0]["id"]
    # match_info(match_id)
    # live_score(match_id)
    # commentary(match_id)
    # scorecard(match_id)
    print(current_match_status())