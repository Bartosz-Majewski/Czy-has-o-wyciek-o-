### Czy twoje hasło jest bezpieczne?
Zapisz hasła, które chcesz przetestować w pliku tekstowym passwords.txt.
Program otwiera plik passwords.txt, a następnie przetwarza go linia po linii.
Jeśli hasło spełnia wszystkie wymogi "dobrego hasła" i nie wyciekło ani razu, to powinno zostać zapisane do osobnego pliku o nazwie bezpieczne.txt.

#### Jak program sprawdza czy hasło wyciekło?
Program korzysta z zewnętrznego API "haveibeenpwnd". Program haszuje hasło za pomocą algorytmu sha1.Następnie do serwisu 
haveibeenpwnd wysyła pierwsze pięć haszów hasła. Tylko 5, ponieważ wysłanie całego hasza może spowodować,że hasło wycieknie.
Serwis odpowie wszystkimi końcówkami hashy jakie zna "haveibeenpwnd" wraz z informacją ile razy dane hasło wyciekło.
Nastęnie porównuje czy końcowka naszego hasza zgadza się, z którąś z usyskanych z API. Ostatecznie otrzymijemy inforamcję czy sprawdzane hasło wyciekło.

#### Przyjęte wymogi bezpiecznego hasła:
● Musi mieć odpowiednią długość (minimum 8 znaków).<br>
● Musi zawierać przynajmniej jedną cyfrę.<br>
● Musi zawierać przynajmniej jeden znak specjalny.<br>
● Musi zawierać wielkie i małe litery.<br>

#### Jak uruchomić program?
Pobierz repozytorium, w pliku tekstowym passwords.txt wpisz hasła(każde w nowej linii).
Uruchom plik validators.py

### Wykorzystane technologie:
● Python <br>
● Zewnętrzne API "haveibeenpwnd"
