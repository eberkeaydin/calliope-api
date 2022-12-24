## Projeyi kendi lokalinizde çalıştırmak için aşağıdaki adımları izleyiniz.

#### Öncelikle pcnizde projeyi indireceğiniz bir klasör oluşturunuz. Klasör konumu dizini örneği: C:\users\eba\Desktop\calliope
#### VsCode'a girip terminali açınız. CMD, Powershell, Bash vb terminaller de tercih edilebilir.
#### cd komutu ile az önce yarattığınız dizine geliniz. ör: `cd \users\eba\Desktop\calliope`
#### `git clone https://github.com/eberkeaydin/calliope-api.git`  --> projeyi klonlayınız.
#### İndirmenin ardından yaratılan projeyi VsCode'da açınız.


#### Projeyi ayağa kaldırmak için Python environmenti kurmak gereklidir. venv kurulumu tavsiye edilir.
#### Pcnizde Python ve pip kurulumlarının bulunması gerekir. `python -v` ve `pip -V` komutları ile versiyon kontrolü yapabilirsiniz.
#### Sorunsuz ayağa kaldırmak için pcnizdeki Python sürümünün v.3.9 ve üzeri olmasına dikkat ediniz  
#### Pcnizde Python ve pip kurulumları var ise proje dizininde terminal üzerinden önce :
#### `py -m pip install --user virtualenv` ardından
#### `py -m venv env` komutları calıstırılarak sanal Python ortamları oluşturulur.
#### `.\env\Scripts\activate` komutu ile ortam aktifleştirilir.(Mac için `source venv/bin/activate`) Terminal kapatılıp bir daha açılır.
#### Proje dizininde terminal üzerinden bu kez `pip install django` komutu ile Django indirilir 
#### Proje dizininde `pip install -r requirements.txt` komutu ile proje bağımlılıkları indirilir.
#### Proje dizininde `py manage.py runserver` komutu calıstırılır(Mac için `python manage.py runserver`) ve proje lokal hostta canlıya alınmıs olur.
#### lokal hostte /quiz URL'ine girip son gelişmeleri; /admin URL girip database gelismelerini kontrol edebilirsiniz.

#### Projede admin paneli vasıtası ile veri girişi yapabilirsiniz. Bunun için django admin rolü yaratmanız gerekecektir.
#### Proje dizininde `py manage.py createsuperuser` komutu ile admin oluşturup tarayıcınızdan `localhost/admin` URL'i ile admin paneline girip veri girişi yapabilirsiniz. 


