import json
import pprint
import copy

def Json2Dfs(objs):
    
    paths = list()
    def rec(now):
        if now["children"]:
            # now: D
            nxts = list()
            for nxt in now["children"]:
                # nxt: C, E
                tokens = rec(nxt)
                # Cの場合: tokens: [[A, C], [B, C],,,]
                for token in tokens:
                    # token.append(now["type"])
                    token.insert(0, now["type"])
                    nxts.append(token)
                # [[A, C, D], [B, C, D],,,]
            return nxts

        else:
            return [
                [now["type"]]
            ]
    return rec(objs)






def main():
    with open("./gold/0b687ec4b2f490051a53d114bf64242580c32f28.json", mode="r") as f:
        contents = json.load(f)
    
    for content in contents:
        if content["type"] != "DOCKER-RUN":
            continue
        for tokens in content["children"]:
            if tokens["type"] != "BASH-SCRIPT":
                continue
            for token in tokens["children"]:
                print()
                print("**************************************************************")
                pprint.pprint(token)
                results = Json2Dfs(token)
                print()
                for result in results:
                    print(result)
                print()
                print("**************************************************************")
                






if __name__ == "__main__":
    main()