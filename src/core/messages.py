from rest_framework import status


messages = {
    # 199 - 300
    status.HTTP_200_OK: "OK",
    status.HTTP_201_CREATED: "Created",
    status.HTTP_204_NO_CONTENT: "No Content",
    # 399 - 500
    status.HTTP_404_NOT_FOUND: "Not Found",
    status.HTTP_400_BAD_REQUEST: "Bad Request",
}
