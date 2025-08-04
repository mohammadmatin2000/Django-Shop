from storages.backends.s3boto3 import S3Boto3Storage
# ======================================================================================================================+
class PublicMediaStorage(S3Boto3Storage):
    bucket_name = 'mybucket'
    custom_domain = '127.0.0.1:9000/mybucket'

    def url(self, name, parameters=None, expire=3600, http_method='GET'):
        url = super().url(name, parameters=parameters, expire=expire, http_method=http_method)
        # force http (remove https if هست)
        if url.startswith('https://'):
            url = 'http://' + url[len('https://'):]
        return url

# ======================================================================================================================
