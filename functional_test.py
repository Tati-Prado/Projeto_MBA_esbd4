from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By  # Adicione esta linha
import unittest
import time

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Safari()
        self.browser.implicitly_wait(10)  # Espera até 10 segundos para carregar elementos

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith acessa a página inicial da aplicação
        self.browser.get('http://127.0.0.1:5000')
        
        # Imprime o título da página para verificar o que está carregando
        print("Título da página carregada:", self.browser.title)
        
        # Ela vê que o título menciona 'To-Do' com prioridades
        self.assertIn('Priority To-Do', self.browser.title)
        
        # Ela é convidada a inserir uma tarefa e a prioridade
        inputbox = self.browser.find_element(By.ID, 'new_task')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a task'
        )
        
        # Ela insere uma tarefa e define a prioridade
        inputbox.send_keys('Comprar anzol')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

if __name__ == '__main__':
    unittest.main(warnings='ignore')
    