# super-resolution-web-public
使用[Real-CUGAN](https://github.com/bilibili/ailab/tree/main/Real-CUGAN)模型`up2x-latest-no-denoise.pth`版本的web application。目前部署的是cpu版，处理1080p->4k大约要20秒。

## 直接访问
[sr-orenji](http://sr-orenji.ml:6990/)

## 关联
[orenji_bot](https://github.com/buptorange/orenji_bot)和[sirius](https://github.com/vayske/sirius)会调用此服务。

## 额外
为了在m1 macos的gpu下部署，我尝试着将原作者的pytorch模型转为onnx再转为了tensorflow模型。你可以在本repo的`tensorflow`下找到`up2x-latest-no-denoise.pth`的tf版，以及runtime wrapper。

但请注意，macos下的tensorflow-metal在面对特大图片输入时会报dimension>2^31错误，目前我还未解决。

runtime dependencies（安装请移步[Install tensorflow on macos with gpu enabled](https://developer.apple.com/metal/tensorflow-plugin/)）:
- `tensorflow-metal==0.4.0`
- `tensorflow-macos==2.8.0`
- `tensorflow-deps==2.8.0`
