from sqlalchemy_media import Image, ImageAnalyzer, ImageValidator, \
    ImageProcessor, AttachmentList


class PlaceImage(Image):
    __pre_processors__ = [
        ImageAnalyzer(),
        ImageValidator(
            minimum=(80, 80),
            maximum=(4096, 4096),
            content_types=['image/jpeg', 'image/png']
        ),
        ImageProcessor(
            fmt='jpeg',
            width=1024,
        )
    ]


class PlaceImageList(AttachmentList):
    __item_type__ = PlaceImage
