from bs4 import BeautifulSoup

def test_get_json_data_button(client1):
    # Get the initial page
    initial_response = client1.get('/')
    assert initial_response.status_code == 200

    # Parse the initial HTML
    initial_soup = BeautifulSoup(initial_response.data, 'html.parser')

    # Find the button
    button = initial_soup.find('button', string='Get JSON Data')
    assert button is not None, "Button 'Get JSON Data' not found"

    # Get the hx-get attribute
    hx_get_url = button.get('hx-get')
    assert hx_get_url == '/data', "Button doesn't have the correct hx-get attribute"

    # Simulate clicking the button by making a GET request to the hx-get URL
    json_response = client1.get(hx_get_url)
    assert json_response.status_code == 200

    # Update the initial HTML with the JSON response (simulating HTMX behavior)
    output_div = initial_soup.find('div', id='output')
    output_div.string = json_response.get_data(as_text=True)
