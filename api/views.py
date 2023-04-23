from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import subprocess
import sys
import os
from django.http import HttpResponse
from django.views import View


class MyAsyncView(View):
    async def get(self, request):
        data = await run_code()
        return HttpResponse(data)


async def run_code():
    """
    Run code with terminal and print all text
    :return:
    """
    proc = subprocess.Popen(['python', '-m', 'autogpt'], stdout=subprocess.PIPE)
    while True:
        line = proc.stdout.readline()
        if not line:
            break
        # декодируем байты в строку
        decoded_line = line.decode('utf-8')
        # the real code does filtering here
        print("test:", decoded_line.rstrip())


class ApiGetText(APIView):

    def get(self, request, *args, **kwargs):
        """This method is called when an HTTP POST request is received.

                The method retrieves the text data from the request data and returns an HTTP
                response with a status code of 400 if the text data is not present, or a status
                code of 200 if the text data is present.

                Args:
                    request: The HTTP request object.
                    *args: Optional arguments.
                    **kwargs: Optional keyword arguments.

                Returns:
                    A Response object containing the appropriate status code.
                """
        text = request.GET.get('text')
        if text is None:
            return Response(status=400)
        if text == 'start':
            run_code()

        return Response(status=200)


class ApiSendText(APIView):
    @staticmethod
    def run_docker():
        """This method is used to run a Docker container using a specified image.

        The Docker command being used runs the container in interactive mode (-it),
        specifies an environment variable file (--env-file), mounts a volume from the
        host file system (-v), and specifies the Docker image to use (autogpt).

        Returns:
            None
        """

        os.system("python -m auto_gpt.autogpt")
        command = 'python -m auto_gpt.autogpt'
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        print(result.decode('utf-8'))

    def get(self, request, *args, **kwargs):
        """This method is called when an HTTP POST request is received.

                The method retrieves the text data from the request data and returns an HTTP
                response with a status code of 400 if the text data is not present, or a status
                code of 200 if the text data is present.

                Args:
                    request: The HTTP request object.
                    *args: Optional arguments.
                    **kwargs: Optional keyword arguments.

                Returns:
                    A Response object containing the appropriate status code.
                """
        text = request.GET.get('text')
        if text is None:
            return Response(status=400)
        self.run_docker()
        return Response(status=200)
