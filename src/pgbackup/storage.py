import sys


def local(in_file, out_file):
    out_file.write(in_file.read())
    out_file.close()
    in_file.close()


def s3(client, infile, bucket, filename):
    try:
        client.head_bucket(Bucket=bucket)
    except:
        print("Bucket does not exit!")
        sys.exit(1)

    client.upload_fileobj(infile, bucket, filename)
