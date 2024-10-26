from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import time

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Safari()
        self.browser.implicitly_wait(10)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith acessa a página inicial da aplicação
        self.browser.get('http://127.0.0.1:5000')
        
        # Ela vê que o título menciona 'To-Do' com prioridades
        self.assertIn('Priority To-Do', self.browser.title)

        # Ela é convidada a inserir uma tarefa e a prioridade
        inputbox = self.browser.find_element(By.ID, 'new_task')
        priority_select = self.browser.find_element(By.ID, 'priority')

        # Edith adiciona "Comprar anzol" com prioridade alta
        inputbox.send_keys('Comprar anzol')
        priority_select.send_keys('High')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # A página atualiza e mostra a tarefa com prioridade alta
        task_list = self.browser.find_element(By.ID, 'task_list')
        tasks = task_list.find_elements(By.TAG_NAME, 'li')

        # Exibe o conteúdo de cada tarefa encontrada para depuração
        for task in tasks:
            print("Conteúdo da tarefa encontrada:", task.text)

        self.assertTrue(
            any(task.text == '1 - Comprar anzol - prioridade alta' for task in tasks),
            "A tarefa 'Comprar anzol' com prioridade alta não foi encontrada."
        )

        # Edith adiciona "Comprar cola instantânea" com prioridade baixa
        inputbox = self.browser.find_element(By.ID, 'new_task')
        inputbox.send_keys('Comprar cola instantânea')
        priority_select.send_keys('Low')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # A página atualiza e mostra ambos os itens com as prioridades corretas
        tasks = task_list.find_elements(By.TAG_NAME, 'li')
        self.assertIn('2 - Comprar cola instantânea - prioridade baixa', [task.text for task in tasks])

        # Edith nota um URL único para sua lista e acessa para confirmar que a lista persiste
        unique_url = self.browser.find_element(By.ID, 'unique_url').text
        self.assertTrue(unique_url)

        self.browser.get(unique_url)
        time.sleep(1)
        tasks = task_list.find_elements(By.TAG_NAME, 'li')
        self.assertIn('1 - Comprar anzol - prioridade alta', [task.text for task in tasks])
        self.assertIn('2 - Comprar cola instantânea - prioridade baixa', [task.text for task in tasks])

if __name__ == '__main__':
    unittest.main(warnings='ignore')
