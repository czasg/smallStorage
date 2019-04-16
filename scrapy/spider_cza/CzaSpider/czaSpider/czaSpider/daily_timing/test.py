from czaSpider.czaTools import *


if __name__ == "__main__":
    while True:
        while True:
            now = datetime.datetime.now()

            if now.hour==9 and now.minute==5:
                break
            print("now, it is no time yet")
            time.sleep(60)

        print("it is time to working...")
