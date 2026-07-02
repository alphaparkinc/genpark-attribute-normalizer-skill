from client import AttributeNormalizerClient
def main():
    c = AttributeNormalizerClient()
    print(c.normalize("size", "extra large"))
if __name__ == '__main__':
    main()
