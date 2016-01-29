# Delorean python

une implémentation de delorean en python

# Lancer les tests

    py.test --cov=delorean
    

# Produire un rapport html de la couverture de test

    py.test --cov=delorean --cov-report html
    
# TODOs V1.1.0

## BUG selecteur

- Corriger le bug du selecteur temporel pour que les tests passent

## Ajout lentille gravitationnelle

- ajouter la méthode ``enable_antigravity_lens(self)`` dans la classe ``Delorean``
- ajouter la méthode ``disable_antigravity_lens(self)`` dans la classe ``Delorean``
- ajouter la méthode ``is_flying(self)`` dans la classe ``Delorean`` qui 
  renvoie ``True`` quand la lentille est activée.
- ajouter le test ``test_delorean_antigravity()`` dans ``delorean_test.py``

## Amélioration du réacteur en reacteur à déchets

- remplacer la méthode ``insert_plutonium(self)`` par la méthode ``insert_waste(self)`` dans la classe ``Delorean``
- remplacer la méthode ``has_plutonium(self)`` par la méthode ``has_waste(self)`` dans la classe ``Delorean``
- remplacer la méthode ``test_delorean_insert_plutonium()`` par la méthode ``test_delorean_insert_waste(self)`` dans ``delorean_test.py``


## Ajout climatisation

- ajouter la méthode ``set_temperature(self, temperature)`` dans la classe ``Delorean``
- ajouter la méthode ``get_temperature(self)`` dans la classe ``Delorean``
- ajouter le test ``test_delorean_temperature()`` dans ``delorean_test.py``

