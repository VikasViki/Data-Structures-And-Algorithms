def main():
    testcases = int(input())
    for _ in range(testcases):
        tablets,budget = map(int,input().split())
        max_area =  -1
        for tablet in range(tablets):
            width,height,price = map(int,input().split())
            if price <= budget:
                area =  width*height
                if area > max_area:
                    max_area = area
        if max_area == -1:
            print("no tablet")
        else:
            print(max_area)
        


if __name__ == "__main__":
    main()
