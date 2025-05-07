from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def Remplir_champ_global_search(texte):
    seleniumlib = BuiltIn().get_library_instance("SeleniumLibrary")
    driver = seleniumlib.driver

    max_attempts = 30
    delay = 1

    for attempt in range(max_attempts):
        try:
            print(f"[{attempt+1}/{max_attempts}] Tentative d'accès au champ de recherche...")

            # Traversée du Shadow DOM imbriqué pour atteindre l'input de recherche globale
            input_element = driver.execute_script("""
                try {
                    // Niveau 1 : composant principal
                    const root1 = document.querySelector("macroponent-f51912f4c700201072b211d4d8c26010");
                    if (!root1) return null;
                    const shadow1 = root1.shadowRoot;

                    // Niveau 2 : layout global
                    const layout = shadow1.querySelector("sn-canvas-appshell-root > sn-canvas-appshell-layout > sn-polaris-layout");
                    if (!layout) return null;
                    const shadow2 = layout.shadowRoot;

                    // Niveau 3 : en-tête de page
                    const header = shadow2.querySelector("sn-polaris-header");
                    if (!header) return null;
                    const shadow3 = header.shadowRoot;

                    // Niveau 4 : wrapper du champ de recherche
                    const wrapper = shadow3.querySelector("sn-search-input-wrapper");
                    if (!wrapper) return null;
                    const shadow4 = wrapper.shadowRoot;

                    // Niveau 5 : composant de saisie typeahead
                    const typeahead = shadow4.querySelector("sn-component-workspace-global-search-typeahead");
                    if (!typeahead) return null;
                    const shadow5 = typeahead.shadowRoot;

                    // Champ de recherche
                    const input = shadow5.querySelector("#sncwsgs-typeahead-input");
                    if (!input) return null;

                    input.focus();
                    return input;
                } catch(e) {
                    return null;
                }
            """)

            if input_element:
                # On récupère la référence JS pour que Selenium puisse y envoyer du texte
                element_ref = driver.execute_script("return arguments[0];", input_element)
                element_ref.clear()
                element_ref.send_keys(texte)
                print("Texte saisi avec succès.")
                return

        except Exception as e:
            print(f"Erreur Python : {e}")

        time.sleep(delay)

    raise Exception("Impossible de trouver ou remplir le champ de recherche global après plusieurs tentatives.")

def Cliquer_sur_bouton_all():
    from robot.libraries.BuiltIn import BuiltIn
    import time

    seleniumlib = BuiltIn().get_library_instance("SeleniumLibrary")
    driver = seleniumlib.driver

    max_attempts = 30
    delay = 0.3

    for attempt in range(max_attempts):
        try:
            print(f"[{attempt+1}/{max_attempts}] Tentative de clic sur le bouton 'All'...")

            bouton_all = driver.execute_script("""
                try {
                    const root1 = document.querySelector("macroponent-f51912f4c700201072b211d4d8c26010");
                    if (!root1) return null;
                    const shadow1 = root1.shadowRoot;

                    const layout = shadow1.querySelector("sn-canvas-appshell-root > sn-canvas-appshell-layout > sn-polaris-layout");
                    if (!layout) return null;
                    const shadow2 = layout.shadowRoot;

                    const header = shadow2.querySelector("sn-polaris-header");
                    if (!header) return null;
                    const shadow3 = header.shadowRoot;

                    const bouton = shadow3.querySelector("#d6e462a5c3533010cbd77096e940dd8c");
                    if (!bouton) return null;

                    bouton.click();
                    return true;
                } catch(e) {
                    return null;
                }
            """)

            if bouton_all:
                print("Clic sur le bouton 'All' réussi.")
                return

        except Exception as e:
            print(f"Erreur lors du clic : {e}")

        time.sleep(delay)

    raise Exception("Échec du clic sur le bouton 'All' après plusieurs tentatives.")



@keyword
def Rechercher_et_selectionner_creer_QT():
    seleniumlib = BuiltIn().get_library_instance("SeleniumLibrary")
    driver = seleniumlib.driver

    max_attempts = 30
    delay = 0.3

    for attempt in range(max_attempts):
        print(f"[{attempt+1}/{max_attempts}] Tentative d’accès à la barre de recherche contextuelle...")

        try:
            input_element = driver.execute_script("""
                try {
                    const root1 = document.querySelector("macroponent-f51912f4c700201072b211d4d8c26010");
                    if (!root1) return null;
                    const shadow1 = root1.shadowRoot;

                    const layout = shadow1.querySelector("sn-canvas-appshell-root > sn-canvas-appshell-layout > sn-polaris-layout");
                    if (!layout) return null;
                    const shadow2 = layout.shadowRoot;

                    const header = shadow2.querySelector("sn-polaris-header");
                    if (!header) return null;
                    const shadow3 = header.shadowRoot;

                    const menu = shadow3.querySelector("nav > div > div.starting-header-zone > sn-polaris-menu:nth-child(2)");
                    if (!menu) return null;
                    const shadow4 = menu.shadowRoot;

                    const input = shadow4.querySelector("#filter");
                    if (!input) return null;

                    input.focus();
                    input.value = "";
                    input.dispatchEvent(new Event('input', { bubbles: true }));
                    return input;
                } catch(e) {
                    return null;
                }
            """)

            if input_element:
                js_input = driver.execute_script("return arguments[0];", input_element)
                js_input.send_keys("Créer QT")
                print("Texte 'Créer QT' saisi dans la barre contextuelle.")
                break

        except Exception as e:
            print(f"Erreur JS : {e}")

        time.sleep(delay)
    else:
        raise Exception("Impossible d’accéder à la barre contextuelle après avoir cliqué sur 'All'.")

    for attempt in range(max_attempts):
        print(f"[{attempt+1}/{max_attempts}] Tentative de clic sur le favori 'Créer QT'...")
        try:
            result = driver.execute_script("""

                try {
                    const root1 = document.querySelector("body > macroponent-f51912f4c700201072b211d4d8c26010")
.shadowRoot.querySelector("div > sn-canvas-appshell-root > sn-canvas-appshell-layout > sn-polaris-layout")
.shadowRoot.querySelector("div.sn-polaris-layout.polaris-enabled > div.layout-main > div.header-bar > sn-polaris-header")
.shadowRoot.querySelector("nav > div > div.starting-header-zone > sn-polaris-menu.is-main-menu.can-animate")
.shadowRoot.querySelector("#favoriteResults > div > div.sn-polaris-tab-content.-left.is-visible.can-animate > div > sn-collapsible-list")
.shadowRoot.querySelector("ul > li > span > a")
console.log("_____")
console.log(root1)
console.log("_____")
root1.click();



return true;

                    const items = shadow5.querySelectorAll("span > span");

                    for (const item of items) {
                        const text = item.innerText.trim().toLowerCase();
                        
                        if (text.includes("créer qt")) {
                            item.click();
                            return true;
                        }
                    }

                    return false;
                } catch(e) {
                console.log(e)
                    return false;
                }
                """)
            if result:
                print("Clic sur 'Créer QT' dans les favoris réussi.")
                return

        except Exception as e:
            print(f"Erreur lors du clic sur 'Créer QT' : {e}")

        time.sleep(delay)

    raise Exception("Impossible de cliquer sur 'Créer QT' dans les favoris.")

@keyword
def switch_to_main_iframe(driver):
    iframe = driver.execute_script("""
        return document
            .querySelector("body > macroponent-f51912f4c700201072b211d4d8c26010")
            .shadowRoot
            .querySelector("#gsft_main");
    """)
    if not iframe:
        raise Exception("Iframe introuvable dans le Shadow DOM.")
    driver.switch_to.frame(iframe)

def remplir_champ_input_id_contrat(driver, wait):
    champ_input_id = "IO:092d612ddbf6ab00a466fda41d961979"
    wait.until(EC.presence_of_element_located((By.ID, champ_input_id)))
    driver.execute_script(f"""
        let el = document.querySelector("[id='{champ_input_id}']");
        el.value = "610000000001";
        el.dispatchEvent(new Event('change', {{ bubbles: true }}));
    """)

def remplir_champ_origine(driver, wait):
    origine_id = "IO:7d9e616ddbf6ab00a466fda41d9619ef"
    wait.until(EC.presence_of_element_located((By.ID, origine_id)))
    driver.execute_script(f"""
        let select = document.querySelector("[id='{origine_id}']");
        for (let option of select.options) {{
            if (option.text.trim() === "Mail") {{
                select.value = option.value;
                select.dispatchEvent(new Event('change', {{ bubbles: true }}));
                break;
            }}
        }}
    """)

def attendre_et_remplir_categorie(driver, wait):
    categorie_id = "IO:3e313daddbf6ab00a466fda41d96190a"
    hidden_id = f"sys_original.{categorie_id}"

    print("Attente du champ catégorie dans le DOM...")

    success = driver.execute_async_script(f"""
        var callback = arguments[arguments.length - 1];
        const start = Date.now();

        function checkOptions() {{
            const select = document.querySelector("select[id='{categorie_id}']");
            if (!select) {{
                if (Date.now() - start > 10000) return callback(false);
                return setTimeout(checkOptions, 300);
            }}
            const options = select.options;
            if (!options || options.length === 0) {{
                if (Date.now() - start > 10000) return callback(false);
                return setTimeout(checkOptions, 300);
            }}
            for (let opt of options) {{
                if (opt.textContent.trim() && opt.textContent.trim() !== "Problème sur le RDV") {{
                    return callback(true);
                }}
            }}
            if (Date.now() - start > 10000) return callback(false);
            setTimeout(checkOptions, 300);
        }}

        checkOptions();
    """)

    if not success:
        raise Exception("Catégorie non peuplée après 30 secondes")

    driver.execute_script(f"""
        const select = document.querySelector("select[id='{categorie_id}']");
        const hidden = document.querySelector("input[id='sys_original.{categorie_id}']");

        if (!select) throw "Sélecteur non trouvé : select[id='{categorie_id}']";
        if (!hidden) throw "Sélecteur non trouvé : input[id='sys_original.{categorie_id}']";

        for (let option of select.options) {{
            if (option.textContent.trim() === "Problème sur le RDV") {{
                select.value = option.value;
                hidden.value = option.value;
                select.dispatchEvent(new Event('change', {{ bubbles: true }}));
                break;
            }}
        }}
    """)

def attendre_et_remplir_sous_categorie(driver, wait):
    sous_categorie_id = "IO:24f1716ddbf6ab00a466fda41d9619fb"
    hidden_id = f"sys_original.{sous_categorie_id}"

    print("Attente du champ sous-catégorie dans le DOM...")

    success = driver.execute_async_script(f"""
        var callback = arguments[arguments.length - 1];
        const start = Date.now();

        function checkOptions() {{
            const select = document.querySelector("select[id='{sous_categorie_id}']");
            if (!select) {{
                if (Date.now() - start > 10000) return callback(false);
                return setTimeout(checkOptions, 300);
            }}
            const options = select.options;
            if (!options || options.length === 0) {{
                if (Date.now() - start > 10000) return callback(false);
                return setTimeout(checkOptions, 300);
            }}
            for (let opt of options) {{
                if (opt.textContent.trim() && opt.textContent.trim() !== "Absence") {{
                    return callback(true);
                }}
            }}
            if (Date.now() - start > 10000) return callback(false);
            setTimeout(checkOptions, 300);
        }}

        checkOptions();
    """)

    if not success:
        raise Exception("Sous-catégorie non peuplée après 40 secondes")
    driver.execute_script(f"""
        const select = document.querySelector("select[id='{sous_categorie_id}']");
        const hidden = document.querySelector("input[id='sys_original.{sous_categorie_id}']");

        if (!select) throw "Sélecteur non trouvé : select[id='{sous_categorie_id}']";
        if (!hidden) throw "Sélecteur non trouvé : input[id='sys_original.{sous_categorie_id}']";

        for (let option of select.options) {{
            if (option.textContent.trim() === "Absence") {{
                select.value = option.value;
                hidden.value = option.value;
                select.dispatchEvent(new Event('change', {{ bubbles: true }}));
                break;
            }}
        }}
    """)

def remplir_champ_technologie(driver, wait):
    technologie_id = "IO:22cde52ddbf6ab00a466fda41d961943"
    hidden_id = f"sys_original.{technologie_id}"

    # Attendre que le champ apparaisse dans le DOM
    wait.until(EC.presence_of_element_located((By.ID, technologie_id)))

    driver.execute_script("""
        const select = document.querySelector("select[id='IO:22cde52ddbf6ab00a466fda41d961943']");
        const hidden = document.querySelector("input[id='sys_original.IO:22cde52ddbf6ab00a466fda41d961943']");

        if (!select) throw "Sélecteur non trouvé : select[id='IO:...']";
        if (!hidden) throw "Sélecteur non trouvé : input[id='sys_original.IO:...']";

        for (let option of select.options) {
            if (option.text.trim() === "ADSL") {
                select.value = option.value;
                hidden.value = option.value;
                select.dispatchEvent(new Event('change', { bubbles: true }));
                break;
            }
        }
    """)
def remplir_description(driver, wait):
    textarea_id = "IO:10f33921db3aab00a466fda41d9619ce"
    hidden_input_id = "sys_original.IO:10f33921db3aab00a466fda41d9619ce"

    # Attendre que le champ description soit présent dans le DOM
    wait.until(EC.presence_of_element_located((By.ID, textarea_id)))

    driver.execute_script(f"""
        const textarea = document.getElementById("{textarea_id}");
        const hidden = document.getElementById("{hidden_input_id}");
        if (!textarea || !hidden) {{
            throw new Error("Champs de description non trouvés");
        }}
        textarea.value = "Ticket test automatisé créer QT par Robotframework";
        hidden.value = "Ticket test automatisé créer QT par Robotframework";
        textarea.dispatchEvent(new Event('input', {{ bubbles: true }}));
        textarea.dispatchEvent(new Event('change', {{ bubbles: true }}));
    """)


def cocher_case_test_ticket(driver, wait):
    checkbox_id = "ni.IO:be8589b9db23a380a466fda41d9619b8"

    # Attendre que l’élément soit présent dans le DOM
    checkbox = wait.until(EC.presence_of_element_located((By.ID, checkbox_id)))

    # Vérifier s’il est déjà coché
    if not checkbox.is_selected():
        # Clic forcé via JavaScript (contourne les superpositions)
        driver.execute_script("arguments[0].click();", checkbox)

def soumettre_ticket(driver, wait):
    wait.until(EC.presence_of_element_located((By.ID, "submit_button")))
    driver.execute_script('document.getElementById("submit_button").click();')


def remplir_champs_obligatoires_QT():
    seleniumlib = BuiltIn().get_library_instance("SeleniumLibrary")
    driver = seleniumlib.driver
    wait = WebDriverWait(driver, 20)

    switch_to_main_iframe(driver)
    remplir_champ_input_id_contrat(driver, wait)
    #remplir_champ_origine(driver, wait)
    remplir_champ_technologie(driver, wait)
    attendre_et_remplir_categorie(driver, wait)
    attendre_et_remplir_sous_categorie(driver, wait)
    #attendre_et_remplir_categorie(driver, wait)
    remplir_description(driver, wait)
    cocher_case_test_ticket(driver, wait)
    soumettre_ticket(driver, wait)
    print("Tous les champs obligatoires ont été remplis.")

