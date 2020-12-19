# BarcodeScanner

A simple Barcode Scanner application using python, opencv and pyzbar. For detailed explanation check out my [blog]().

This was possible only due to the simple and clear explanation by Adrian Rosebrock's [blog](https://www.pyimagesearch.com/2018/05/21/an-opencv-barcode-and-qr-code-scanner-with-zbar/).

## How to run?

### 1. Create virtual environment

```shell
python3 -m venv venv
```

#### macOS
```shell
source venv/bin/activate
```

#### Windows
```shell
.\venv\Scripts\activate
```

### 2. Install required dependencies

```shell
pip3 install -r requirements.txt
```

### 3. Execute

#### a. To detect faces from Images
```shell
python3 -m scan_images -i /path/to/image/file.jpg
```

#### b. To detect faces from Videos

###### i. To detect faces from video files
```shell
python3 -m scan_videos -v /path/to/video/file.mov
```

###### ii. To detect faces realtime using camera
```shell
python3 -m scan_videos
```
