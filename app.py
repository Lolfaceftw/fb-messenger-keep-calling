import pyautogui
import time

TIMEOUT = 5
CONFIDENCE_LEVEL = 0.95
def find_and_click(image_path: str) -> bool:
    while True:
        try:
            print(f"Finding {image_path}...")
            location = pyautogui.locateCenterOnScreen(image_path, confidence=CONFIDENCE_LEVEL)
            if location:
                print(f"Found {image_path} @ {location}.")
                print("Clicking...")
                pyautogui.click(location)
                print("Clicked.")
                return True
        except pyautogui.ImageNotFoundException:
            time.sleep(0.2)
            print(f"Image @ {image_path} not found.")
        except Exception as e:
            print(f"Error! {e}")

def main(*args, **kwargs) -> None:
    if find_and_click("video_cam.png") == True:
        while True:
            find_and_click("redial.png")

if __name__ == "__main__":
    main()
    
