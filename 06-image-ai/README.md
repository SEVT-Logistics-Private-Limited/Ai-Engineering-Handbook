# 06 — Image AI and Computer Vision

## Learning path
1. What an image file contains; raster vs vector graphics
2. Pixels, width, height, channels, RGB, grayscale and alpha
3. Color spaces, bit depth, resolution and compression
4. Decoding and preprocessing: resize, crop, normalize and augment
5. Image tensors: shape, dtype, value range and channel order
6. Computer vision tasks: classification, localization, detection and segmentation
7. Convolution, kernels, feature maps and pooling
8. CNN architecture and transfer learning
9. Vision Transformers and patch embeddings
10. Image embeddings, contrastive learning and image-text alignment
11. Evaluation: accuracy, precision/recall, IoU and mAP (as appropriate)

## Conceptual image pipeline
Image file → decoder → pixel array/tensor → model-specific preprocessing → vision model/encoder → task head or visual representation → prediction or downstream multimodal component.

The exact pipeline depends on the model. Some models use convolutional feature maps; others divide images into patches or use multiple crops.

## Practical labs
- Open an image with Pillow and inspect dimensions, mode and pixel values.
- Convert RGB to grayscale and compare channel shapes.
- Resize and normalize an image according to a model's documented requirements.
- Visualize a convolution kernel and resulting feature map.
- Run an image classifier and inspect confidence scores responsibly.

## VLM connection
A vision-language model combines visual information with language. Document the specific vision encoder, image preprocessing, visual-token or feature interface, language component and inference path used by the model being studied. Do not assume all VLMs share one architecture.
