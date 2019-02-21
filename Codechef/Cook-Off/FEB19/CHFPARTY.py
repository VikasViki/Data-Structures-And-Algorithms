## Question : https://www.codechef.com/COOK103B/problems/CHFPARTY/

def main():
    testcases = int(input())
    for test in range(testcases):
        no_of_friends = int(input())
        friends = list(map(int,input().split()))
        people_at_party = 0
        friends.sort()
        for friend in friends:
            if people_at_party >= friend:
                people_at_party += 1
            else:
                break
        print(people_at_party)

if __name__ == "__main__":
    main()
