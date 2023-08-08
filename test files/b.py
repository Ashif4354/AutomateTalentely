import win32api
import win32con

def get_windows_resolution():
    width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
    return width, height

if __name__ == "__main__":
    width, height = get_windows_resolution()
    print(f"The Windows resolution is {width}x{height}")
