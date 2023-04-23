from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import subprocess


class ApiGetText(APIView):
    @staticmethod
    def run_docker():
        """This method is used to run a Docker container using a specified image.

        The Docker command being used runs the container in interactive mode (-it),
        specifies an environment variable file (--env-file), mounts a volume from the
        host file system (-v), and specifies the Docker image to use (autogpt).

        Returns:
            None
        """
        command = 'docker run -it --env-file=./.env -v $PWD/auto_gpt_workspace:/home/appuser/auto_gpt_workspace autogpt'
        subprocess.call(command, shell=True)

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
