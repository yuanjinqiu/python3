import qrcode
from PIL import Image

# 设置要生成二维码的网址
url = "https://www.baidu.com"

# 创建QRCode对象
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# 添加网址数据到QRCode对象
qr.add_data(url)
qr.make(fit=True)

# 创建二维码图像
qr_image = qr.make_image(fill_color="black", back_color="blue")

# 加载Logo图像
logo_path = "logo.png"  # 替换为您的Logo图像路径
logo_image = Image.open(logo_path)

# 调整Logo的大小
logo_size = (qr_image.size[0] // 4, qr_image.size[1] // 4)
logo_image = logo_image.resize(logo_size)

# 计算Logo的位置
logo_position = ((qr_image.size[0] - logo_image.size[0]) // 2, (qr_image.size[1] - logo_image.size[1]) // 2)

# 将Logo图像合并到二维码图像上
qr_image.paste(logo_image, logo_position)

# 保存带有Logo的二维码图像
qr_image.save("ma.png")
