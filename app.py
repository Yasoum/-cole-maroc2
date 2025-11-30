import streamlit as st
import json
import os
import random
from datetime import datetime

# --- 1. CONFIGURATION ET DONNÉES ---
FICHIER_DONNEES = "ecole_data.json"
MOT_DE_PASSE_ADMIN = "admin123"

# Niveaux du système marocain primaire
NIVEAUX = ["1AP (CP)", "2AP (CE1)", "3AP (CE2)", "4AP (CM1)", "5AP (CM2)", "6AP (6AEP)"]

# --- 2. GÉNÉRATEUR D'HISTOIRES LONGUES ET CONTEXTUALISÉES ---
def generer_histoires():
    histoires = {}
    
    # Bases de données pour la variation
    prenoms = ["Ahmed", "Fatima", "Youssef", "Aya", "Mehdi", "Khadija", "Omar", "Salma", "Driss", "Leïla"]
    villes = ["Rabat", "Casablanca", "Marrakech", "Fès", "Tanger", "Agadir", "Chefchaouen", "Dakhla"]
    plats = ["un délicieux Couscous", "un Tajine aux pruneaux", "une Pastilla", "une Harira chaude", "du thé à la menthe"]
    lieux = ["l'école", "la mosquée", "le souk", "le jardin public", "la montagne de l'Atlas", "la plage"]

    for niveau in NIVEAUX:
        histoires[niveau] = []
        
        # On détermine la complexité du texte selon le niveau
        est_petit = "1AP" in niveau or "2AP" in niveau
        est_moyen = "3AP" in niveau or "4AP" in niveau
        
        for i in range(1, 21): # 20 histoires par niveau
            
            # Choix aléatoire des éléments pour cette histoire
            hero = random.choice(prenoms)
            ami = random.choice([p for p in prenoms if p != hero])
            ville = random.choice(villes)
            plat = random.choice(plats)
            lieu = random.choice(lieux)
            
            # Construction du titre
            titre = f"Histoire {i} : {hero} et {ami} à {ville}"
            
            # Construction du contenu (Long et Détaillé)
            if est_petit:
                # Niveau CP/CE1 : Histoires simples mais complètes (~100-150 mots)
                contenu = f"""
                **Chapitre 1 : Le matin**
                Aujourd'hui est un jour très spécial pour {hero}. Le soleil brille fort dans le ciel bleu de {ville}. 
                {hero} se réveille tôt, fait sa toilette et met ses beaux vêtements. Maman a préparé un bon petit-déjeuner avec du pain, de l'huile d'olive et du thé.
                
                **Chapitre 2 : La rencontre**
                En sortant de la maison pour aller à {lieu}, {hero} rencontre son ami {ami}. 
                « Bonjour {ami} ! » dit {hero} avec un grand sourire. « Est-ce que tu veux venir avec moi ? »
                {ami} est très content et répond : « Oui, bien sûr ! Allons-y ensemble. C'est toujours plus amusant d'être à deux. »
                
                **Chapitre 3 : Une belle journée**
                Arrivés à destination, ils jouent et discutent joyeusement. Ils voient des chats qui dorment à l'ombre et des oiseaux qui chantent.
                À midi, ils rentrent chez eux pour manger {plat}. {hero} est très fatigué mais très heureux de cette belle journée.
                Il a appris que l'amitié est un trésor précieux.
                """
                questions = [
                    {"q": f"Où habite {hero} ?", "opts": [ville, "Paris", "Londres"], "a": ville},
                    {"q": f"Qui est l'ami de {hero} ?", "opts": [ami, "Mickey", "Personne"], "a": ami},
                    {"q": "Que mangent-ils à midi ?", "opts": [plat, "Une pizza", "Des frites"], "a": plat},
                    {"q": "Quel temps fait-il ?", "opts": ["Il pleut", "Le soleil brille", "Il neige"], "a": "Le soleil brille"},
                    {"q": "Quelle est la leçon de l'histoire ?", "opts": ["L'amitié est précieuse", "Il faut dormir", "Il faut manger"], "a": "L'amitié est précieuse"}
                ]

            elif est_moyen:
                # Niveau CE2/CM1 : Histoires plus riches (~200-250 mots)
                contenu = f"""
                **Introduction**
                Il était une fois, dans la magnifique ville de {ville}, un enfant nommé {hero}. {hero} était connu pour sa grande curiosité et sa gentillesse. 
                Chaque année, pendant les vacances, {hero} aimait explorer de nouveaux endroits. Cette année, l'aventure se déroulait vers {lieu}.
                
                **Le Problème**
                Alors qu'ils marchaient, {hero} et {ami} trouvèrent un petit oiseau blessé sur le chemin. L'oiseau ne pouvait plus voler. 
                « Oh non, pauvre petit ! » s'écria {ami}. « Nous ne pouvons pas le laisser ici, il y a trop de dangers. »
                {hero} réfléchit un instant et dit : « Tu as raison. Nous devons l'aider. C'est notre devoir de protéger la nature et les animaux. »
                
                **La Solution**
                Avec beaucoup de douceur, ils prirent l'oiseau et le ramenèrent à la maison. Ils lui donnèrent de l'eau et quelques graines.
                Pendant plusieurs jours, ils s'occupèrent de lui après l'école. Grand-mère était fière d'eux et leur prépara {plat} pour les récompenser de leur bon cœur.
                
                **Conclusion**
                Finalement, l'oiseau guérit. Un matin, il déploya ses ailes et s'envola vers le ciel bleu. {hero} et {ami} étaient un peu tristes de le voir partir, mais ils savaient qu'ils avaient fait une bonne action.
                Cette histoire nous apprend qu'il faut toujours aider ceux qui sont plus faibles que nous.
                """
                questions = [
                    {"q": "Que trouvent les enfants ?", "opts": ["Un oiseau blessé", "Un chat", "Un chien"], "a": "Un oiseau blessé"},
                    {"q": "Quelle qualité a {hero} ?", "opts": ["La gentillesse", "La colère", "La paresse"], "a": "La gentillesse"},
                    {"q": "Où se passe l'histoire ?", "opts": [ville, "Au pôle Nord", "En Chine"], "a": ville},
                    {"q": "Qui prépare le repas ?", "opts": ["Grand-mère", "Le voisin", "Le boulanger"], "a": "Grand-mère"},
                    {"q": "Que fait l'oiseau à la fin ?", "opts": ["Il s'envole", "Il reste", "Il dort"], "a": "Il s'envole"}
                ]

            else:
                # Niveau CM2/6AEP : Histoires complexes, valeurs civiques (~300+ mots)
                contenu = f"""
                **Chapitre 1 : Les préparatifs de la fête**
                C'était bientôt la grande fête nationale à {ville}. Les rues étaient décorées de drapeaux rouges avec l'étoile verte. 
                Tout le monde s'activait pour préparer l'événement. {hero}, qui était maintenant en classe de 6e année, avait été choisi pour lire un poème devant toute l'école.
                C'était un grand honneur, mais aussi une grande responsabilité. {hero} avait le trac et peur d'oublier son texte.
                
                **Chapitre 2 : La difficulté**
                La veille de la fête, {hero} n'arrivait pas à dormir. « Et si je me trompe ? Et si tout le monde se moque de moi ? » pensait-il.
                Son ami {ami} vint le voir pour le rassurer. « Écoute, {hero}, tu as travaillé dur. Tu connais ton texte par cœur. L'important n'est pas d'être parfait, mais d'être sincère. »
                {ami} aida {hero} à répéter encore une fois, en lui donnant courage et confiance. Ils partagèrent ensemble {plat} pour se donner des forces.
                
                **Chapitre 3 : Le grand jour**
                Le jour J arriva. L'école était pleine de parents et de professeurs. Quand le directeur appela {hero} sur l'estrade, le silence se fit.
                {hero} prit une grande inspiration, regarda {ami} qui lui faisait un signe de pouce levé, et commença à lire.
                Sa voix était claire et forte. Il parla de l'amour de la patrie, du respect des aînés et de l'importance de l'éducation pour l'avenir du Maroc.
                
                **Conclusion et Morale**
                Quand il finit, tout le monde applaudit très fort. Le professeur félicita {hero} pour son courage.
                Ce jour-là, {hero} comprit que le soutien des amis et le travail sérieux permettent de surmonter toutes les peurs. 
                Il comprit aussi que servir son école et son pays est la plus grande des fiertés.
                """
                questions = [
                    {"q": "Quel événement se prépare ?", "opts": ["Une fête nationale", "Un anniversaire", "Un match de foot"], "a": "Une fête nationale"},
                    {"q": "Pourquoi {hero} a-t-il peur ?", "opts": ["Il doit lire un poème", "Il est malade", "Il a perdu son sac"], "a": "Il doit lire un poème"},
                    {"q": "Comment {ami} aide-t-il {hero} ?", "opts": ["Il l'encourage", "Il se moque", "Il part"], "a": "Il l'encourage"},
                    {"q": "De quoi parle le poème ?", "opts": ["Amour de la patrie", "Recette de cuisine", "Jeux vidéo"], "a": "Amour de la patrie"},
                    {"q": "Quelle est la morale ?", "opts": ["Le travail paie", "Il faut tricher", "Il ne faut rien faire"], "a": "Le travail paie"}
                ]

            histoires[niveau].append({
                "id": f"{niveau}_{i}",
                "titre": titre,
                "contenu": contenu,
                "quiz": questions
            })
            
    return histoires

STORIES_DB = generer_histoires()

# --- 3. GESTION DES DONNÉES (JSON) ---
def charger_donnees():
    if not os.path.exists(FICHIER_DONNEES):
        return {"users": [], "results": []}
    with open(FICHIER_DONNEES, "r") as f:
        return json.load(f)

def sauvegarder_donnees(data):
    with open(FICHIER_DONNEES, "w") as f:
        json.dump(data, f, indent=4)

# --- 4. FONCTIONS UTILITAIRES ---
def trouver_utilisateur(username, data):
    for user in data["users"]:
        if user["username"] == username:
            return user
    return None

def calculer_erreurs_totales(student_username, data):
    total_fautes = 0
    for res in data["results"]:
        if res["student"] == student_username:
            total_fautes += res["fautes"]
    return total_fautes

# --- 5. INTERFACE PRINCIPALE ---
st.set_page_config(page_title="École Numérique Maroc", page_icon="🇲🇦", layout="wide")

if "user" not in st.session_state:
    st.session_state.user = None

data = charger_donnees()

# --- BARRE LATÉRALE ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/194/194935.png", width=100)
    st.title("📚 École en Ligne")
    
    if st.session_state.user:
        st.success(f"👤 {st.session_state.user['username']}")
        st.info(f"Rôle : {st.session_state.user['role'].upper()}")
        if st.button("Se déconnecter"):
            st.session_state.user = None
            st.rerun()
    else:
        choix_menu = st.radio("Menu", ["Connexion", "Inscription Élève", "Inscription Professeur", "Admin"])

# --- LOGIQUE DES PAGES ---

# 1. PAGE DE CONNEXION / INSCRIPTION
if not st.session_state.user:
    st.header("Bienvenue sur la plateforme de lecture")
    st.write("Le système éducatif numérique pour le primaire.")
    
    if choix_menu == "Connexion":
        with st.form("login_form"):
            user_input = st.text_input("Nom d'utilisateur")
            pass_input = st.text_input("Mot de passe", type="password")
            submitted = st.form_submit_button("Se connecter")
            
            if submitted:
                u = trouver_utilisateur(user_input, data)
                if u and u["password"] == pass_input:
                    st.session_state.user = u
                    st.rerun()
                else:
                    st.error("Identifiants incorrects.")

    elif choix_menu == "Inscription Élève":
        st.subheader("Nouvel Élève 🎓")
        with st.form("reg_student"):
            new_user = st.text_input("Choisis un nom d'utilisateur")
            new_pass = st.text_input("Choisis un mot de passe", type="password")
            niveau = st.selectbox("Ton niveau scolaire", NIVEAUX)
            submit = st.form_submit_button("S'inscrire")
            
            if submit:
                if trouver_utilisateur(new_user, data):
                    st.error("Ce nom existe déjà.")
                elif new_user and new_pass:
                    data["users"].append({
                        "username": new_user,
                        "password": new_pass,
                        "role": "eleve",
                        "niveau": niveau,
                        "date_inscription": str(datetime.now())
                    })
                    sauvegarder_donnees(data)
                    st.success("Inscription réussie ! Connecte-toi maintenant.")

    elif choix_menu == "Inscription Professeur":
        st.subheader("Nouveau Professeur 👨‍🏫")
        with st.form("reg_prof"):
            new_user = st.text_input("Nom d'utilisateur (Prof)")
            new_pass = st.text_input("Mot de passe", type="password")
            niveau = st.selectbox("Niveau de la classe enseignée", NIVEAUX)
            submit = st.form_submit_button("Créer compte Professeur")
            
            if submit:
                if trouver_utilisateur(new_user, data):
                    st.error("Ce nom existe déjà.")
                elif new_user and new_pass:
                    data["users"].append({
                        "username": new_user,
                        "password": new_pass,
                        "role": "prof",
                        "niveau": niveau
                    })
                    sauvegarder_donnees(data)
                    st.success("Compte Professeur créé !")

    elif choix_menu == "Admin":
        st.subheader("Espace Administrateur 🛡️")
        pass_admin = st.text_input("Mot de passe Admin", type="password")
        if pass_admin == MOT_DE_PASSE_ADMIN:
            st.session_state.user = {"username": "Admin", "role": "admin"}
            st.rerun()

# 2. ESPACE ÉLÈVE
elif st.session_state.user["role"] == "eleve":
    user = st.session_state.user
    st.title(f"👋 Bonjour {user['username']} !")
    st.info(f"Tu es en classe de : {user['niveau']}")
    
    mes_histoires = STORIES_DB[user["niveau"]]
    titres = [h["titre"] for h in mes_histoires]
    choix_histoire = st.selectbox("Choisis une histoire à lire :", titres)
    histoire_actuelle = next(h for h in mes_histoires if h["titre"] == choix_histoire)
    
    st.markdown("---")
    st.header(histoire_actuelle["titre"])
    st.markdown(histoire_actuelle["contenu"]) # Utilisation de markdown pour le formatage
    
    st.markdown("---")
    st.subheader("📝 Le Quiz")
    
    deja_fait = False
    for res in data["results"]:
        if res["student"] == user["username"] and res["story_id"] == histoire_actuelle["id"]:
            st.warning(f"Tu as déjà fait ce quiz. Note : {res['score']}/5 (Fautes: {res['fautes']})")
            deja_fait = True
    
    if not deja_fait:
        with st.form("quiz_student"):
            reponses = {}
            for idx, q in enumerate(histoire_actuelle["quiz"]):
                st.write(f"**Question {idx+1} :** {q['q']}")
                reponses[idx] = st.radio("Réponse", q["opts"], key=f"q_{idx}", label_visibility="collapsed")
            
            submit_quiz = st.form_submit_button("Valider mes réponses")
            
            if submit_quiz:
                score = 0
                fautes = 0
                for idx, q in enumerate(histoire_actuelle["quiz"]):
                    if reponses[idx] == q["a"]:
                        score += 1
                    else:
                        fautes += 1
                
                data["results"].append({
                    "student": user["username"],
                    "story_id": histoire_actuelle["id"],
                    "story_title": histoire_actuelle["titre"],
                    "score": score,
                    "fautes": fautes,
                    "date": str(datetime.now())
                })
                sauvegarder_donnees(data)
                
                if fautes == 0:
                    st.balloons()
                    st.success("Bravo ! 5/5 !")
                else:
                    st.error(f"Tu as fait {fautes} erreur(s). Relis bien le texte !")
                st.rerun()

# 3. ESPACE PROFESSEUR
elif st.session_state.user["role"] == "prof":
    prof = st.session_state.user
    st.title(f"👨‍🏫 Tableau de bord - {prof['niveau']}")
    st.markdown("### 📋 Suivi de la classe")
    
    eleves_classe = [u for u in data["users"] if u["role"] == "eleve" and u["niveau"] == prof["niveau"]]
    
    if not eleves_classe:
        st.warning("Aucun élève inscrit dans ce niveau pour le moment.")
    else:
        # Affichage en colonnes pour faire plus "Pro"
        col1, col2 = st.columns(2)
        for i, eleve in enumerate(eleves_classe):
            fautes_totales = calculer_erreurs_totales(eleve["username"], data)
            histoires_lues = [r for r in data["results"] if r["student"] == eleve["username"]]
            
            # Alterne les colonnes
            with (col1 if i % 2 == 0 else col2):
                with st.container(border=True):
                    st.subheader(f"🎓 {eleve['username']}")
                    st.write(f"**Histoires lues :** {len(histoires_lues)}")
                    
                    if fautes_totales > 5:
                        st.error(f"⚠️ **ALERTE :** {fautes_totales} fautes cumulées.")
                    else:
                        st.success(f"✅ **Stable :** {fautes_totales} fautes.")
                        
                    with st.expander("Voir détails"):
                        if not histoires_lues:
                            st.write("Aucune activité.")
                        for h in histoires_lues:
                            color = "green" if h["fautes"] == 0 else "red"
                            st.markdown(f"- :{color}[{h['story_title']}] : {h['score']}/5")

# 4. ESPACE ADMIN
elif st.session_state.user["role"] == "admin":
    st.title("🛡️ Administration")
    
    all_users = data["users"]
    if not all_users:
        st.write("Aucun utilisateur.")
    
    for i, u in enumerate(all_users):
        with st.container(border=True):
            c1, c2, c3, c4 = st.columns([1, 2, 2, 1])
            c1.write(f"**{u['role'].upper()}**")
            c2.write(u['username'])
            c3.write(u.get('niveau', 'Admin'))
            if c4.button("Supprimer", key=f"del_{i}"):
                data["users"].pop(i)
                data["results"] = [r for r in data["results"] if r["student"] != u["username"]]
                sauvegarder_donnees(data)
                st.success("Supprimé.")
                st.rerun()