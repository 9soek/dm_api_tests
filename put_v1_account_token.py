import requests


def put_v1_account_token():
      """
      Activate registered user
      :return:
      """


  token = '123123123'
  url = f"http://5.63.153.31:5051/v1/account/{token}"

  headers = {
      'X-Dm-Auth-Token': '<string>',
      'X-Dm-Bb-Render-Mode': '<string>',
      'Accept': 'text/plain'
  }

  response = requests.request(
      method="PUT",
      url=url,
      headers=headers
  )

  print(response.text)
