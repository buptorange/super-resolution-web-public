from io import BytesIO

import numpy
import tensorflow as tf
import numpy as np
import cv2

class ModelWrapper(object):
    def __init__(self, abs_model_file_path: str):
        self.model = tf.saved_model.load(abs_model_file_path, tags=None, options=None)

    def np2tensor(self,np_frame):
        tensor = tf.convert_to_tensor(np.transpose(np_frame, (2, 0, 1)), dtype=tf.float32)
        tensor = tf.expand_dims(tensor, 0)
        return tensor / 255

    def tensor2np(self,tensor):
        tensor = tf.squeeze(tensor*255.0)
        tensor = tf.math.round(tensor)
        tensor = tf.clip_by_value(tensor, 0, 255)
        tensor = tf.cast(tensor, tf.uint8)
        return np.transpose(tensor.numpy(), (1,2,0))

    def __call__(self, image_bytes: bytes):
        img_buffer_numpy = np.frombuffer(image_bytes, dtype=np.uint8)  # 将 图片字节码bytes  转换成一维的numpy数组 到缓存中
        frame = cv2.imdecode(img_buffer_numpy, 1)[:, :, [2, 1, 0]]
        print(frame.shape)
        tensor = self.np2tensor(frame)
        try:
            result = self.tensor2np(self.model(x=tensor)["img"])[:, :, ::-1]
        except Exception as e:
            raise e
        _, img_encode = cv2.imencode('.jpg', result)
        img_bytes = img_encode.tobytes()
        return img_bytes