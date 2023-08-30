from plyer import notification
import time

if __name__ == '__main__':
     while True:
          notification.notify(
               title="*** Take Rest ***",
               message="Rest is vital for better metal health, refresh mind and make more workable",
               timeout=5)
          time.sleep(20)
     print("hi")

#pythonw file_name