from django.shortcuts import render


# def home(request):
#     return render(
#         request,
#         "main_app/home.html",
#         {
#             "websocket_url": "wss://ijiklmdla1.execute-api.us-west-2.amazonaws.com/production/"
#         },
#     )
def home(request):
    return render(
        request,
        "main_app/home.html",
        {
            "websocket_url": "wss://n36t0unjfl.execute-api.ap-northeast-2.amazonaws.com/llm/"
        },
    )
