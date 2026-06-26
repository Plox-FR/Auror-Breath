"""
Cohérence Cardiaque v1.0 — AUROR Breath (Bottom-Right Anchor Edition)
- Nom : AUROR Breath
- Auteur : Paul CAUSSE (Plox-FR)
- Audio libre de droits: lasonotheque.org
"""
import tkinter as tk
from tkinter import ttk
import math
import time
import threading
import webbrowser
import os
import sys
import winsound
import random

# Liens de soutien
PAYPAL_URL = "paypal.me/PloxFR"
KOFI_URL   = "ko-fi.com/polocse"

# Dimensions de référence
BASE_W = 400
MENU_H = 600  
EXEC_H = 340  

# Palettes de couleurs premium
BG_MAIN      = "#0d0b21"  # Fond ultra-dark spatial
BG_CARD      = "#161233"  # Fond des sections/cartes
ACCENT       = "#6366f1"  # Violet Indigo moderne
ACCENT_HOVER = "#4f46e5"  # Indigo plus sombre au survol
TEXT_MUTED   = "#6b7280"  # Gris neutre
TEXT_LIGHT   = "#9ca3af"  # Gris clair doux
TEXT_WHITE   = "#ffffff"  # Blanc pur

LOCALES = {
    "FR": {
        "title": "AUROR BREATH",
        "welcome": "Prenez un instant pour vous recentrer.",
        "sec_exercise": "EXERCICE DE RESPIRATION",
        "sec_duration": "DURÉE DE LA SESSION",
        "sec_sound": "AMBIANCE SONORE",
        "sec_size": "TAILLE DE L'INTERFACE",
        "btn_start": "LANCER LA SESSION  ▶",
        "btn_paypal": "💳  Soutenir le projet (Paypal)",
        "btn_kofi": "☕  Offrir un café (Ko-fi)",
        "dur_eq": "5 Min",
        "dur_stress": "2 Min",
        "dur_free": "Libre",
        "sound_birds": "Oiseaux",
        "sound_sea": "Mer",
        "sound_rain": "Pluie",
        "sound_night": "Nuit",
        "size_l": "Grand",
        "size_m": "Moyen",
        "size_s": "Petit",
        "size_xs": "Mini",
        "phase_in": "INSPIREZ",
        "phase_hold_f": "RETENEZ (PLEIN)",
        "phase_out": "EXPIREZ",
        "phase_hold_e": "RETENEZ (VIDE)",
        "cycle": "Cycle",
        "ex_cc": "Cohérence Cardiaque [5-0-5-0]",
        "ex_ei": "Équilibre Intérieur [4-0-4-0]",
        "ex_re": "Relaxation Express [3-0-6-0]",
        "ex_sp": "Soupir Physiologique [4-1-6-0]",
        "ex_cc2": "Calme Clair [5-0-7-0]",
        "ex_as": "Anti-Stress Flash [4-4-6-0]",
        "ex_sn": "Sédatif naturel [4-7-8-0]",
        "ex_sp2": "Sommeil Profond [4-0-6-0]",
        "ex_ap": "Ancrage Profond [5-2-5-2]",
        "ex_rt": "Respiration Triangle [4-4-4-0]",
        "ex_rc": "Respiration Carrée [4-4-4-4]",
        "ex_rci": "Respiration Carrée Intense [5-5-5-5]",
        "ex_fm": "Focus Mental [6-2-7-0]",
        "ex_fe": "Flux Énergisant [6-0-4-0]",
        "ex_em": "Éveil Matinal [5-3-3-0]",
        "desc_cc": "Rééquilibre le système nerveux et réduit l'anxiété.",
        "desc_ei": "Harmonisation rapide et retour au calme neutre.",
        "desc_re": "Relâchement musculaire et mental ultra-rapide.",
        "desc_sp": "Double inspiration pour réinitialiser le stress.",
        "desc_cc2": "Allonge l'expiration pour apaiser l'esprit.",
        "desc_as": "Idéal face à une urgence pour faire baisser la pression.",
        "desc_sn": "Un sédatif naturel parfait pour stopper le flux de pensées.",
        "desc_sp2": "Ralentit le rythme cardiaque pour l'endormissement.",
        "desc_ap": "Stabilise l'esprit et renforce la présence à soi.",
        "desc_rt": "Structure le souffle pour développer la concentration.",
        "desc_rc": "Utilisée pour retrouver un focus absolu sous la pression.",
        "desc_rci": "Variante intense pour une maîtrise totale des émotions.",
        "desc_fm": "Augmente la capacité d'attention prolongée.",
        "desc_fe": "Dynamise l'organisme et stimule la clarté mentale.",
        "desc_em": "Idéal au réveil pour oxygéner le cerveau efficacement.",
        "goal_reached": "Objectif Atteint !",
        "btn_menu": "Retour au Menu",
        "btn_quit": "Quitter l'application"
    },
    "GB": {
        "title": "AUROR BREATH",
        "welcome": "Take a moment to center yourself.",
        "sec_exercise": "BREATHING EXERCISE",
        "sec_duration": "SESSION DURATION",
        "sec_sound": "SOUND AMBIANCE",
        "sec_size": "INTERFACE SIZE",
        "btn_start": "START SESSION  ▶",
        "btn_paypal": "💳  Support the project (Paypal)",
        "btn_kofi": "☕  Buy a coffee (Ko-fi)",
        "dur_eq": "5 Min",
        "dur_stress": "2 Min",
        "dur_free": "Free",
        "sound_birds": "Birds",
        "sound_sea": "Ocean",
        "sound_rain": "Rain",
        "sound_night": "Night",
        "size_l": "Large",
        "size_m": "Medium",
        "size_s": "Small",
        "size_xs": "Mini",
        "phase_in": "INHALE",
        "phase_hold_f": "HOLD (FULL)",
        "phase_out": "EXHALE",
        "phase_hold_e": "HOLD (EMPTY)",
        "cycle": "Cycle",
        "ex_cc": "Cardiac Coherence [5-0-5-0]",
        "ex_ei": "Inner Balance [4-0-4-0]",
        "ex_re": "Express Relaxation [3-0-6-0]",
        "ex_sp": "Physiological Sigh [4-1-6-0]",
        "ex_cc2": "Clear Calm [5-0-7-0]",
        "ex_as": "Flash Anti-Stress [4-4-6-0]",
        "ex_sn": "Natural Sedative [4-7-8-0]",
        "ex_sp2": "Deep Sleep [4-0-6-0]",
        "ex_ap": "Deep Grounding [5-2-5-2]",
        "ex_rt": "Triangle Breathing [4-4-4-0]",
        "ex_rc": "Box Breathing [4-4-4-4]",
        "ex_rci": "Intense Box Breathing [5-5-5-5]",
        "ex_fm": "Mental Focus [6-2-7-0]",
        "ex_fe": "Energizing Flow [6-0-4-0]",
        "ex_em": "Morning Wake-Up [5-3-3-0]",
        "desc_cc": "Balances the nervous system and reduces anxiety.",
        "desc_ei": "Quick stabilization and return to neutral calm.",
        "desc_re": "Ultra-fast muscle and mental release.",
        "desc_sp": "Double inhalation to instantly reset stress.",
        "desc_cc2": "Lengthens expiration to soothe the mind.",
        "desc_as": "Ideal for emergencies to lower pressure quickly.",
        "desc_sn": "A natural sedative to stop racing thoughts.",
        "desc_sp2": "Slows down heart rate to ease into sleep.",
        "desc_ap": "Stabilizes the mind and strengthens self-presence.",
        "desc_rt": "Structures the breath to develop concentration.",
        "desc_rc": "Used to regain absolute focus under pressure.",
        "desc_rci": "Intense variant for total emotional control.",
        "desc_fm": "Increases prolonged attention span.",
        "desc_fe": "Energizes the body and stimulates mental clarity.",
        "desc_em": "Ideal upon waking to oxygenate the brain efficiently.",
        "goal_reached": "Goal Achieved!",
        "btn_menu": "Back to Menu",
        "btn_quit": "Exit Application"
    },
    "ES": {
        "title": "AUROR BREATH",
        "welcome": "Tómate un momento para centrarte.",
        "sec_exercise": "EJERCICIO DE RESPIRACIÓN",
        "sec_duration": "DURACIÓN DE LA SESIÓN",
        "sec_sound": "AMBIENTE SONORO",
        "sec_size": "TAMAÑO DE INTERFAZ",
        "btn_start": "INICIAR SESIÓN  ▶",
        "btn_paypal": "💳  Apoyar el proyecto (Paypal)",
        "btn_kofi": "☕  Invitar un café (Ko-fi)",
        "dur_eq": "5 Min",
        "dur_stress": "2 Min",
        "dur_free": "Libre",
        "sound_birds": "Pájaros",
        "sound_sea": "Mar",
        "sound_rain": "Lluvia",
        "sound_night": "Noche",
        "size_l": "Grande",
        "size_m": "Medio",
        "size_s": "Pequeño",
        "size_xs": "Mini",
        "phase_in": "INHALA",
        "phase_hold_f": "RETÉN (LLENO)",
        "phase_out": "EXHALA",
        "phase_hold_e": "RETÉN (VACÍO)",
        "cycle": "Ciclo",
        "ex_cc": "Coherencia Cardíaca [5-0-5-0]",
        "ex_ei": "Equilibrio Interior [4-0-4-0]",
        "ex_re": "Relajación Express [3-0-6-0]",
        "ex_sp": "Suspiro Fisiológico [4-1-6-0]",
        "ex_cc2": "Calma Clara [5-0-7-0]",
        "ex_as": "Antiestrés Flash [4-4-6-0]",
        "ex_sn": "Sedante Natural [4-7-8-0]",
        "ex_sp2": "Sueño Profundo [4-0-6-0]",
        "ex_ap": "Anclaje Profundo [5-2-5-2]",
        "ex_rt": "Respiración Triangular [4-4-4-0]",
        "ex_rc": "Respiración Cuadrada [4-4-4-4]",
        "ex_rci": "Respiración Cuadrada Intensa [5-5-5-5]",
        "ex_fm": "Enfoque Mental [6-2-7-0]",
        "ex_fe": "Flujo Energizante [6-0-4-0]",
        "ex_em": "Despertar Matutino [5-3-3-0]",
        "desc_cc": "Equilibra el sistema nervioso y reduce la ansiedad.",
        "desc_ei": "Armonización rápida y retorno a la calma.",
        "desc_re": "Relajación muscular y mental ultrarrápida.",
        "desc_sp": "Doble intención para reiniciar el estrés.",
        "desc_cc2": "Alarga la exhalación para calmar la mente.",
        "desc_as": "Ideal para emergencies para bajar la presión.",
        "desc_sn": "Sedante natural para frenar pensamientos limitantes.",
        "desc_sp2": "Ralentiza el ritmo cardíaco para el sueño.",
        "desc_ap": "Estabiliza la mente y refuerza la presencia.",
        "desc_rt": "Estructura la respiración para la concentration.",
        "desc_rc": "Usada para recuperar un enfoque absoluto bajo presión.",
        "desc_rci": "Variante intensa para control emotional completo.",
        "desc_fm": "Aumenta la capacidad de atención prolongada.",
        "desc_fe": "Dinamiza el organismo y estimula la claridad mental.",
        "desc_em": "Ideal al despertar para oxigenar el cerebro.",
        "goal_reached": "¡Objetivo Logrado!",
        "btn_menu": "Volver al Menú",
        "btn_quit": "Salir de la Aplicación"
    },
    "DE": {
        "title": "AUROR BREATH",
        "welcome": "Nehmen Sie sich einen Moment Zeit, um sich zu sammeln.",
        "sec_exercise": "ATEMÜBUNG",
        "sec_duration": "SITZUNGSDAUER",
        "sec_sound": "SOUND-AMBIENTE",
        "sec_size": "OBERFLÄCHENGRÖSSE",
        "btn_start": "SITZUNG STARTEN  ▶",
        "btn_paypal": "💳  Projekt unterstützen (Paypal)",
        "btn_kofi": "☕  Kaffee ausgeben (Ko-fi)",
        "dur_eq": "5 Min",
        "dur_stress": "2 Min",
        "dur_free": "Frei",
        "sound_birds": "Vögel",
        "sound_sea": "Meer",
        "sound_rain": "Regen",
        "sound_night": "Nacht",
        "size_l": "Groß",
        "size_m": "Mittel",
        "size_s": "Klein",
        "size_xs": "Mini",
        "phase_in": "EINATMEN",
        "phase_hold_f": "HALTEN (VOLL)",
        "phase_out": "AUSATMEN",
        "phase_hold_e": "HALTEN (LEER)",
        "cycle": "Zyklus",
        "ex_cc": "Herzkohärenz [5-0-5-0]",
        "ex_ei": "Innere Balance [4-0-4-0]",
        "ex_re": "Express-Entspannung [3-0-6-0]",
        "ex_sp": "Physiologischer Seufzer [4-1-6-0]",
        "ex_cc2": "Klare Ruhe [5-0-7-0]",
        "ex_as": "Anti-Stress Flash [4-4-6-0]",
        "ex_sn": "Natürliches Beruhigungsmittel [4-7-8-0]",
        "ex_sp2": "Tiefschlaf [4-0-6-0]",
        "ex_ap": "Tiefe Erdung [5-2-5-2]",
        "ex_rt": "Dreiecksatmung [4-4-4-0]",
        "ex_rc": "Quadratische Atmung [4-4-4-4]",
        "ex_rci": "Intensive Quadratatmung [5-5-5-5]",
        "ex_fm": "Mentaler Fokus [6-2-7-0]",
        "ex_fe": "Energetisierter Fluss [6-0-4-0]",
        "ex_em": "Morgendliches Erwachen [5-3-3-0]",
        "desc_cc": "Gleicht das Nervensystem aus und reduziert Angstzustände.",
        "desc_ei": "Schnelle Stabilisierung und Rückkehr zur Ruhe.",
        "desc_re": "Ultraschnelle muskuläre und mentale Entspannung.",
        "desc_sp": "Doppeltes Einatmen, um Stress sofort zurückzusetzen.",
        "desc_cc2": "Verlängert das Ausatmen, um den Geist zu beruhigen.",
        "desc_as": "Ideal bei Notfällen, um den Druck schnell zu senken.",
        "desc_sn": "Perfekt, um kreisende Gedanken zu stoppen.",
        "desc_sp2": "Verlangsamt den Herzschlag, um das Einschlafen zu erleichtern.",
        "desc_ap": "Stabilisiert den Geist und stärkt die Selbstpräsenz.",
        "desc_rt": "Strukturiert den Atem, um die Konzentration zu fördern.",
        "desc_rc": "Wird verwendet, um unter Druck den Fokus wiederzuerlangen.",
        "desc_rci": "Intensive Variante für totale emotionale Kontrolle.",
        "desc_fm": "Erhöht die anhaltende Aufmerksamkeitsspanne.",
        "desc_fe": "Dynamisiert den Körper und fördert die mentale Klarheit.",
        "desc_em": "Ideal nach dem Aufwachen, um das Gehirn effizient zu versorgen.",
        "goal_reached": "Ziel Erreicht!",
        "btn_menu": "Zurück zum Menü",
        "btn_quit": "Anwendung Beenden"
    },
    "IT": {
        "title": "AUROR BREATH",
        "welcome": "Prenditi un momento per centrarti.",
        "sec_exercise": "ESERCIZIO DI RESPIRAZIONE",
        "sec_duration": "DURATA DELLA SESSIONE",
        "sec_sound": "AMBIENTE SONORO",
        "sec_size": "DIMENSIONE INTERFACCIA",
        "btn_start": "AVVIA SESSIONE  ▶",
        "btn_paypal": "💳  Sostieni il progetto (Paypal)",
        "btn_kofi": "☕  Offri un caffè (Ko-fi)",
        "dur_eq": "5 Min",
        "dur_stress": "2 Min",
        "dur_free": "Libero",
        "sound_birds": "Uccelli",
        "sound_sea": "Mare",
        "sound_rain": "Pioggia",
        "sound_night": "Notte",
        "size_l": "Grande",
        "size_m": "Medio",
        "size_s": "Piccolo",
        "size_xs": "Mini",
        "phase_in": "INSPIRA",
        "phase_hold_f": "TRATTENI (PIENO)",
        "phase_out": "ESPIRA",
        "phase_hold_e": "TRATTENI (VUOTO)",
        "cycle": "Ciclo",
        "ex_cc": "Coerenza Cardiaca [5-0-5-0]",
        "ex_ei": "Equilibrio Interiore [4-0-4-0]",
        "ex_re": "Relax Espresso [3-0-6-0]",
        "ex_sp": "Sospiro Fisiologico [4-1-6-0]",
        "ex_cc2": "Calma Chiara [5-0-7-0]",
        "ex_as": "Anti-Stress Flash [4-4-6-0]",
        "ex_sn": "Sedativo Naturale [4-7-8-0]",
        "ex_sp2": "Sonnellino Profondo [4-0-6-0]",
        "ex_ap": "Radicamento Profondo [5-2-5-2]",
        "ex_rt": "Respirazione Triangolare [4-4-4-0]",
        "ex_rc": "Respirazione Quadrata [4-4-4-4]",
        "ex_rci": "Respirazione Quadrata Intensa [5-5-5-5]",
        "ex_fm": "Focus Mentale [6-2-7-0]",
        "ex_fe": "Flusso Energizzante [6-0-4-0]",
        "ex_em": "Risveglio Mattutino [5-3-3-0]",
        "desc_cc": "Rieilibra il sistema nervoso e riduce l'ansia.",
        "desc_ei": "Stabilizzazione rapida e ritorno alla calma neutra.",
        "desc_re": "Rilascio muscolare e mentale ultra-rapido.",
        "desc_sp": "Doppia inspirazione per resettare istantaneamente lo stress.",
        "desc_cc2": "Allunga l'espirazione pour lenire la mente.",
        "desc_as": "Ideale in caso di emergenza pour abbassare la pressione.",
        "desc_sn": "Un sedativo naturale perfetto per fermare i pensieri calcolatori.",
        "desc_sp2": "Rallenta il battito cardiaco per facilitare il sonno.",
        "desc_ap": "Stabilizza la mente e rafforza la presenza di sé.",
        "desc_rt": "Struttura il respiro pour sviluppare la concentrazione.",
        "desc_rc": "Utilizzato per ritrovare il focus assoluto sotto pressione.",
        "desc_rci": "Variante intensa per un controllo emotivo totale.",
        "desc_fm": "Aumenta la capacità di attenzione prolungata.",
        "desc_fe": "Dinamizza l'organismo e stimola la chiarezza mentale.",
        "desc_em": "Ideale al risveglio per ossigenare il cervello in modo efficace.",
        "goal_reached": "Obiettivo Raggiunto!",
        "btn_menu": "Torna al Menu",
        "btn_quit": "Chiudi l'Applicazione"
    },
    "PT": {
        "title": "AUROR BREATH",
        "welcome": "Reserve um momento para se centrar.",
        "sec_exercise": "EXERCÍCIO DE RESPIRACIÓN",
        "sec_duration": "DURAÇÃO DA SESSÃO",
        "sec_sound": "AMBIENTE SONORO",
        "sec_size": "TAMANHO DA INTERFACE",
        "btn_start": "INICIAR SESSÃO  ▶",
        "btn_paypal": "💳  Apoiar o projeto (Paypal)",
        "btn_kofi": "☕  Oferecer um café (Ko-fi)",
        "dur_eq": "5 Min",
        "dur_stress": "2 Min",
        "dur_free": "Livre",
        "sound_birds": "Pássaros",
        "sound_sea": "Mar",
        "sound_rain": "Chuva",
        "sound_night": "Noite",
        "size_l": "Grande",
        "size_m": "Médio",
        "size_s": "Pequeno",
        "size_xs": "Mini",
        "phase_in": "INALE",
        "phase_hold_f": "RETENHA (CHEIO)",
        "phase_out": "EXALE",
        "phase_hold_e": "RETENHA (VAZIO)",
        "cycle": "Ciclo",
        "ex_cc": "Coerência Cardíaca [5-0-5-0]",
        "ex_ei": "Equilíbrio Interior [4-0-4-0]",
        "ex_re": "Relaxamento Expresso [3-0-6-0]",
        "ex_sp": "Suspiro Fisiológico [4-1-6-0]",
        "ex_cc2": "Calma Clara [5-0-7-0]",
        "ex_as": "Anti-Stress Flash [4-4-6-0]",
        "ex_sn": "Sedativo Natural [4-7-8-0]",
        "ex_sp2": "Sono Profundo [4-0-6-0]",
        "ex_ap": "Ancoragem Profunda [5-2-5-2]",
        "ex_rt": "Respiração Triangular [4-4-4-0]",
        "ex_rc": "Respiração Quadrada [4-4-4-4]",
        "ex_rci": "Respiração Quadrada Intensa [5-5-5-5]",
        "ex_fm": "Foco Mental [6-2-7-0]",
        "ex_fe": "Fluxo Energizante [6-0-4-0]",
        "ex_em": "Despertar Matinal [5-3-3-0]",
        "desc_cc": "Equilibra o sistema nervoso e reduz a ansiedade.",
        "desc_ei": "Estabilização rápida e retorno à calma neutra.",
        "desc_re": "Liberação muscular e mental ultra-rápida.",
        "desc_sp": "Dupla inalação para redefinir o estresse instantaneamente.",
        "desc_cc2": "Alonga a expiração para acalmar a mente.",
        "desc_as": "Ideal para emergências para baixar a pressão rapidamente.",
        "desc_sn": "Um sedativo natural perfeito para parar pensamentos acelerados.",
        "desc_sp2": "Desacelera o ritmo cardíaco para facilitar o sono.",
        "desc_ap": "Estabiliza a mente e reforça a presença de si.",
        "desc_rt": "Estrutura a respiração para desenvolver a concentration.",
        "desc_rc": "Usado para recuperar o foco absoluto sob pressão.",
        "desc_rci": "Variante intensa para controle emocional total.",
        "desc_fm": "Aumenta la capacidade de atenção prolongada.",
        "desc_fe": "Dinamiza o organismo e stimula la clareza mental.",
        "desc_em": "Ideal ao acordar para oxigenar o cérebro eficientemente.",
        "goal_reached": "Objetivo Alcançado!",
        "btn_menu": "Voltar ao Menu",
        "btn_quit": "Sair do Aplicativo"
    }
}

MODES_KEYS = [
    ("ex_cc", 5, 0, 5, 0, "desc_cc"), ("ex_ei", 4, 0, 4, 0, "desc_ei"),
    ("ex_re", 3, 0, 6, 0, "desc_re"), ("ex_sp", 4, 1, 6, 0, "desc_sp"),
    ("ex_cc2", 5, 0, 7, 0, "desc_cc2"), ("ex_as", 4, 4, 6, 0, "desc_as"),
    ("ex_sn", 4, 7, 8, 0, "desc_sn"), ("ex_sp2", 4, 0, 6, 0, "desc_sp2"),
    ("ex_ap", 5, 2, 5, 2, "desc_ap"), ("ex_rt", 4, 4, 4, 0, "desc_rt"),
    ("ex_rc", 4, 4, 4, 4, "desc_rc"), ("ex_rci", 5, 5, 5, 5, "desc_rci"),
    ("ex_fm", 6, 2, 7, 0, "desc_fm"), ("ex_fe", 6, 0, 4, 0, "desc_fe"),
    ("ex_em", 5, 3, 3, 0, "desc_em")
]

SKY_NIGHT   = [(26,  18,  58), (42,  20,  80)]
SKY_DAWN    = [(180, 80,  90), (230, 120, 80)]
SKY_DAY     = [(255, 180, 130),(255, 210, 160)]
WATER_NIGHT = (40,  30,  80)
WATER_DAY   = (220, 150, 130)
SUN_INNER   = (255, 255, 255)
SUN_MID     = (255, 220, 180)
SUN_OUTER   = (255, 160, 100)
MOON_INNER  = (245, 248, 255)
MOON_HALO   = (100, 115, 165)
ROCK_DARK   = (55,  35, 100)
ROCK_MID    = (80,  55, 140)
REED_DARK   = (60,  40, 110)
REED_ORANGE = (200, 100, 60)
LILY_COLOR  = (90,  65, 140)

def lerp(a, b, t):
    t = max(0.0, min(1.0, t))
    return a + (b - a) * t

def lerp_rgb(c1, c2, t):
    return tuple(int(lerp(a, b, t)) for a, b in zip(c1, c2))

def rgb(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"

def sky_color(progress):
    if progress < 0.5:
        t = progress * 2
        top = lerp_rgb(SKY_NIGHT[0], SKY_DAWN[0], t)
        bot = lerp_rgb(SKY_NIGHT[1], SKY_DAWN[1], t)
    else:
        t = (progress - 0.5) * 2
        top = lerp_rgb(SKY_DAWN[0], SKY_DAY[0], t)
        bot = lerp_rgb(SKY_DAWN[1], SKY_DAY[1], t)
    return top, bot

def water_color(progress):
    return lerp_rgb(WATER_NIGHT, WATER_DAY, progress)

class CoherenceApp:
    def __init__(self, root):
        self.root = root
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        self.root.resizable(False, False)
        self.root.configure(bg="#2a225c") 

        try:
            if getattr(sys, 'frozen', False):
                icon_path = os.path.join(sys._MEIPASS, "icone.ico")
            else:
                icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icone.ico")
            if os.path.exists(icon_path):
                self.root.iconbitmap(icon_path)
        except Exception:
            pass

        self.scale = 1.0
        self.w = BASE_W
        self.h = MENU_H
        self.lang = "FR"

        # Position absolue d'ancrage fixe (Bas Droit de l'écran)
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        self.fixed_right = sw - 25
        self.fixed_bottom = sh - 65

        # Premier calcul de position du menu principal initial
        x = self.fixed_right - self.w
        y = self.fixed_bottom - self.h
        self.root.geometry(f"{self.w}x{self.h}+{x}+{y}")

        self.root.bind("<ButtonPress-1>", self._drag_start)
        self.root.bind("<B1-Motion>", self._drag_move)

        self.selected_mode_idx = 0
        self.selected_duration_id = "eq"
        self.selected_sound_id = "birds"
        self.selected_size_label = "Grand"
        self.is_muted = False  

        self.running = False
        self.is_paused = False
        self.phase = "idle"
        self.phase_t = 0.0
        self.cycle_count = 0
        self.session_time_elapsed = 0.0
        self._last_tick_time = 0.0

        self.stars = []
        self.rain_drops = []
        self.rain_ripples = []  
        self.birds_fx = []
        self.fireflies = []

        self._after_id = None
        self._sound_thread = None
        self._sound_stop = threading.Event()

        self.container = tk.Frame(self.root, bg=BG_MAIN)
        self.container.pack(fill="both", expand=True, padx=1, pady=1)

        self._show_home_screen()

    def _clear_container(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def _get_txt(self, key):
        return LOCALES[self.lang].get(key, "")

    def _change_language(self, event):
        self.lang = self.combo_lang.get()
        self._show_home_screen()

    def _bind_hover(self, widget, normal_bg, hover_bg):
        widget.bind("<Enter>", lambda e: widget.config(bg=hover_bg) if widget['state'] != 'disabled' else None)
        widget.bind("<Leave>", lambda e: widget.config(bg=normal_bg) if widget['state'] != 'disabled' else None)

    def _show_home_screen(self):
        self._clear_container()
        sc = self.scale

        # Ajustement dynamique des dimensions par le bas droit
        self.w = int(BASE_W * sc)
        if self.selected_size_label == "Mini":
            self.h = 410
        elif self.selected_size_label == "Petit":
            self.h = 430
        else:
            self.h = int(MENU_H * sc)
            
        new_x = self.fixed_right - self.w
        new_y = self.fixed_bottom - self.h
        self.root.geometry(f"{self.w}x{self.h}+{new_x}+{new_y}")

        home_frame = tk.Frame(self.container, bg=BG_MAIN)
        home_frame.pack(fill="both", expand=True, padx=int(18*sc), pady=int(16*sc))

        top_bar = tk.Frame(home_frame, bg=BG_MAIN)
        top_bar.pack(fill="x", pady=(0, int(4*sc)))
        
        lbl_app_title = tk.Label(top_bar, text=self._get_txt("title"), font=("Segoe UI", int(max(12, int(15*sc))), "bold"), bg=BG_MAIN, fg=TEXT_WHITE)
        lbl_app_title.pack(side="left")

        right_menu = tk.Frame(top_bar, bg=BG_MAIN)
        right_menu.pack(side="right")

        style = ttk.Style()
        style.theme_use('default')
        style.configure("Lang.TCombobox", fieldbackground=BG_MAIN, background=BG_MAIN, foreground="white", arrowcolor=ACCENT, borderwidth=0)
        style.map("Lang.TCombobox", fieldbackground=[('readonly', BG_MAIN)], foreground=[('readonly', 'white')])

        lang_options = list(LOCALES.keys())
        
        self.combo_lang = ttk.Combobox(right_menu, values=lang_options, state="readonly", style="Lang.TCombobox", font=("Segoe UI", int(max(9, int(10*sc)))), width=4)
        self.combo_lang.set(self.lang)
        self.combo_lang.pack(side="left", padx=(0, int(4*sc)))
        self.combo_lang.bind("<<ComboboxSelected>>", self._change_language)

        btn_close = tk.Label(right_menu, text="✕", font=("Segoe UI", int(max(12, int(13*sc)))), bg=BG_MAIN, fg=TEXT_LIGHT, cursor="hand2", padx=int(4*sc))
        btn_close.pack(side="left")
        btn_close.bind("<Button-1>", lambda e: self.root.destroy())

        lbl_welcome = tk.Label(home_frame, text=self._get_txt("welcome"), font=("Segoe UI", int(max(8, int(9.5*sc)))), bg=BG_MAIN, fg=TEXT_LIGHT)
        lbl_welcome.pack(anchor="w", pady=(0, int(14*sc)))

        self._create_section_title(home_frame, self._get_txt("sec_exercise"))
        
        self.modes_translated_names = [self._get_txt(m[0]) for m in MODES_KEYS]
        self.mode_var = tk.StringVar(value=self.modes_translated_names[self.selected_mode_idx])
        
        style.configure("Custom.TCombobox", fieldbackground=BG_CARD, background=BG_CARD, foreground="white", arrowcolor=ACCENT, borderwidth=0)
        style.map("Custom.TCombobox", fieldbackground=[('readonly', BG_CARD)], foreground=[('readonly', 'white')])

        combo_mode = ttk.Combobox(home_frame, textvariable=self.mode_var, values=self.modes_translated_names, state="readonly", style="Custom.TCombobox", font=("Segoe UI", int(max(9, int(11*sc)))))
        combo_mode.pack(fill="x", pady=(0, int(4*sc)))
        combo_mode.bind("<<ComboboxSelected>>", self._on_mode_changed)

        desc_key = MODES_KEYS[self.selected_mode_idx][5]
        self.lbl_desc = tk.Label(home_frame, text=self._get_txt(desc_key), font=("Segoe UI", int(max(8, int(9*sc)))), bg=BG_MAIN, fg=ACCENT, height=2, justify="center", wraplength=int(BASE_W * sc - 40))
        self.lbl_desc.pack(fill="x", pady=(0, int(10*sc)))

        self._create_section_title(home_frame, self._get_txt("sec_duration"))
        dur_frame = tk.Frame(home_frame, bg=BG_MAIN)
        dur_frame.pack(fill="x", pady=(0, int(12*sc)))
        
        self.dur_buttons = {}
        durations = [("eq", self._get_txt("dur_eq")), ("stress", self._get_txt("dur_stress")), ("free", self._get_txt("dur_free"))]
        for d_id, d_text in durations:
            btn = tk.Button(
                dur_frame, text=d_text, 
                font=("Segoe UI", int(max(8, int(10*sc))), "bold"), 
                relief="flat", bd=0, highlightthickness=0, takefocus=0,
                cursor="hand2", command=lambda v=d_id: self._set_duration(v)
            )
            btn.pack(side="left", fill="x", expand=True, padx=int(3*sc))
            self.dur_buttons[d_id] = btn
        self._update_dur_styles()

        self._create_section_title(home_frame, self._get_txt("sec_sound"))
        sound_frame = tk.Frame(home_frame, bg=BG_MAIN)
        sound_frame.pack(fill="x", pady=(0, int(12*sc)))

        self.sound_buttons = {}
        sounds = [("birds", "🐦"), ("sea", "🌊"), ("rain", "🌧"), ("night", "🌙")]
        for s_id, s_text in sounds:
            btn = tk.Button(
                sound_frame, text=s_text, 
                font=("Segoe UI", int(max(11, int(13*sc)))), 
                relief="flat", bd=0, highlightthickness=0, takefocus=0,
                cursor="hand2", command=lambda v=s_id: self._set_sound(v)
            )
            btn.pack(side="left", fill="x", expand=True, padx=int(3*sc))
            self.sound_buttons[s_id] = btn
        self._update_sound_styles()

        self._create_section_title(home_frame, self._get_txt("sec_size"))
        size_frame = tk.Frame(home_frame, bg=BG_MAIN)
        size_frame.pack(fill="x", pady=(0, int(18*sc)))

        self.size_buttons = {}
        sizes = [
            ("Grand", 1.0, self._get_txt("size_l")), 
            ("Moyen", 0.82, self._get_txt("size_m")), 
            ("Petit", 0.70, self._get_txt("size_s")),
            ("Mini", 0.55, self._get_txt("size_xs"))
        ]
        for s_label, factor, s_trans in sizes:
            btn = tk.Button(
                size_frame, text=s_trans, 
                font=("Segoe UI", int(max(8, int(9.5*sc)))), 
                relief="flat", bd=0, highlightthickness=0, takefocus=0,
                cursor="hand2", command=lambda f=factor, l=s_label: self._resize_app(f, l)
            )
            btn.pack(side="left", fill="x", expand=True, padx=int(3*sc))
            self.size_buttons[s_label] = btn
        self._update_size_styles()

        btn_start = tk.Button(home_frame, text=self._get_txt("btn_start"), font=("Segoe UI", int(max(10, int(12*sc))), "bold"), bg=ACCENT, fg="white", relief="flat", activebackground=ACCENT_HOVER, activeforeground="white", bd=0, pady=int(9*sc), cursor="hand2", command=self._start_exercise_screen)
        btn_start.pack(fill="x", pady=(0, int(8*sc)))
        self._bind_hover(btn_start, ACCENT, ACCENT_HOVER)

        support_frame = tk.Frame(home_frame, bg=BG_MAIN)
        support_frame.pack(fill="x", side="bottom")

        lbl_author = tk.Label(support_frame, text="Conçu et développé par Paul CAUSSE", font=("Segoe UI", int(max(7, int(8.5*sc)))), bg=BG_MAIN, fg=TEXT_MUTED)
        lbl_author.pack(pady=(0, int(4*sc)))

        btn_paypal = tk.Button(support_frame, text=self._get_txt("btn_paypal"), font=("Segoe UI", int(max(7, int(9*sc)))), bg=BG_CARD, fg=TEXT_LIGHT, relief="flat", activebackground="#1e1845", activeforeground="white", bd=0, pady=int(4*sc), cursor="hand2", command=lambda: webbrowser.open(PAYPAL_URL))
        btn_paypal.pack(fill="x", pady=(0, int(4*sc)))
        self._bind_hover(btn_paypal, BG_CARD, "#1e1845")

        btn_kofi = tk.Button(support_frame, text=self._get_txt("btn_kofi"), font=("Segoe UI", int(max(7, int(9*sc)))), bg=BG_CARD, fg=TEXT_LIGHT, relief="flat", activebackground="#1e1845", activeforeground="white", bd=0, pady=int(4*sc), cursor="hand2", command=lambda: webbrowser.open(KOFI_URL))
        btn_kofi.pack(fill="x")
        self._bind_hover(btn_kofi, BG_CARD, "#1e1845")

    def _create_section_title(self, parent, text):
        sc = self.scale
        lbl = tk.Label(parent, text=text, font=("Segoe UI", int(max(7, int(8.5 * sc))), "bold"), bg=BG_MAIN, fg=TEXT_MUTED)
        lbl.pack(anchor="w", pady=(0, int(5 * sc)))

    def _on_mode_changed(self, event):
        self.selected_mode_idx = self.modes_translated_names.index(self.mode_var.get())
        desc_key = MODES_KEYS[self.selected_mode_idx][5]
        self.lbl_desc.config(text=self._get_txt(desc_key))

    def _set_duration(self, val):
        self.selected_duration_id = val
        self._update_dur_styles()

    def _set_sound(self, val):
        self.selected_sound_id = val
        self._update_sound_styles()

    def _update_dur_styles(self):
        for d, btn in self.dur_buttons.items():
            if d == self.selected_duration_id:
                btn.config(bg=ACCENT, fg="white")
                self._bind_hover(btn, ACCENT, ACCENT)
            else:
                btn.config(bg=BG_CARD, fg=TEXT_LIGHT)
                self._bind_hover(btn, BG_CARD, "#221c4d")

    def _update_sound_styles(self):
        for s, btn in self.sound_buttons.items():
            if s == self.selected_sound_id:
                btn.config(bg=ACCENT, fg="white")
                self._bind_hover(btn, ACCENT, ACCENT)
            else:
                btn.config(bg=BG_CARD, fg=TEXT_LIGHT)
                self._bind_hover(btn, BG_CARD, "#221c4d")

    def _update_size_styles(self):
        for s, btn in self.size_buttons.items():
            if s == self.selected_size_label:
                btn.config(bg=ACCENT, fg="white")
                self._bind_hover(btn, ACCENT, ACCENT)
            else:
                btn.config(bg=BG_CARD, fg=TEXT_LIGHT)
                self._bind_hover(btn, BG_CARD, "#221c4d")

    def _resize_app(self, factor, label):
        self.scale = factor
        self.selected_size_label = label
        
        self.w = int(BASE_W * factor)
        if label == "Mini":
            self.h = 410
        elif label == "Petit":
            self.h = 430
        else:
            self.h = int(MENU_H * factor)
        
        # Recalcul de la géométrie depuis le coin fixe bas-droit
        new_x = self.fixed_right - self.w
        new_y = self.fixed_bottom - self.h
        self.root.geometry(f"{self.w}x{self.h}+{new_x}+{new_y}")
        self._show_home_screen()

    def _init_stars(self, cw, horizon):
        self.stars = []
        for _ in range(35):
            x = random.randint(5, cw - 5)
            y = random.randint(5, horizon - 10)
            size = random.choice([1, 1, 1, 2])
            brightness = random.uniform(0.5, 1.0)
            self.stars.append((x, y, size, brightness))

    def _init_rain(self, cw, ch):
        self.rain_drops = []
        for _ in range(40):
            self.rain_drops.append({
                "x": random.randint(-20, cw),
                "y": random.randint(-20, ch),
                "speed": random.uniform(10, 18),
                "len": random.randint(8, 15)
            })
            
    def _init_rain_ripples(self, cw, horizon, ch):
        self.rain_ripples = []
        for _ in range(12):
            self.rain_ripples.append({
                "x": random.randint(15, cw - 40),
                "y": random.randint(horizon + 5, ch - 15),
                "len": random.randint(10, 24),
                "life": random.uniform(0, math.pi)
            })

    def _init_fireflies(self, cw, horizon, ch):
        self.fireflies = []
        for _ in range(7):
            self.fireflies.append({
                "x": random.uniform(10, cw - 10),
                "y": random.uniform(horizon - 15, ch - 10),
                "angle": random.uniform(0, math.pi * 2),
                "speed": random.uniform(0.4, 1.1),
                "phase": random.uniform(0, math.pi * 2)
            })

    def _update_rain(self, cw, ch):
        for drop in self.rain_drops:
            drop["y"] += drop["speed"]
            drop["x"] += drop["speed"] * 0.15
            if drop["y"] > ch:
                drop["y"] = random.randint(-20, 0)
                drop["x"] = random.randint(-20, cw)

    def _update_rain_ripples(self, cw, horizon, ch):
        for ripple in self.rain_ripples:
            ripple["life"] += 0.09
            if ripple["life"] > math.pi:
                ripple["life"] = 0
                ripple["x"] = random.randint(15, cw - 40)
                ripple["y"] = random.randint(horizon + 5, ch - 15)
                ripple["len"] = random.randint(10, 24)

    def _update_fireflies(self, cw, horizon, ch):
        for f in self.fireflies:
            f["angle"] += random.uniform(-0.4, 0.4)
            f["x"] += math.cos(f["angle"]) * f["speed"]
            f["y"] += math.sin(f["angle"]) * f["speed"] * 0.6
            f["phase"] += random.uniform(0.06, 0.16)

            if f["x"] < 0: f["x"] = cw
            if f["x"] > cw: f["x"] = 0
            if f["y"] < horizon - 25: f["y"] = ch - 10
            if f["y"] > ch: f["y"] = horizon - 25

    def _update_birds_fx(self, cw, horizon):
        if len(self.birds_fx) < 6 and random.random() < 0.08:
            cx = random.choice([-8, cw + 8])
            base_y = random.randint(int(horizon * 0.08), int(horizon * 0.72))
            going_right = (cx < 0)
            num = random.randint(3, 6)
            for i in range(num):
                self.birds_fx.append({
                    "x": cx + random.uniform(-12, 12),
                    "y": base_y + random.uniform(-10, 10),
                    "vx": random.uniform(0.6, 1.4) * (1 if going_right else -1),
                    "vy": random.uniform(-0.25, 0.25),
                    "wing_state": random.uniform(0, math.pi * 2),
                    "turn_timer": random.uniform(30, 90),
                    "alive": True,
                })

        for bird in self.birds_fx[:]:
            bird["vy"] += random.uniform(-0.04, 0.04)
            bird["vy"] = max(-0.5, min(0.5, bird["vy"]))
            bird["x"] += bird["vx"]
            bird["y"] += bird["vy"]
            bird["wing_state"] += random.uniform(0.55, 0.85)
            bird["turn_timer"] -= 1

            if bird["turn_timer"] <= 0:
                bird["vx"] += random.uniform(-0.2, 0.2)
                bird["vx"] = max(0.3, min(1.6, abs(bird["vx"]))) * (1 if bird["vx"] >= 0 else -1)
                bird["turn_timer"] = random.uniform(25, 70)

            if bird["x"] < -20 or bird["x"] > cw + 20 or bird["y"] < 2 or bird["y"] > horizon - 5:
                self.birds_fx.remove(bird)

    def _start_exercise_screen(self):
        self._clear_container()
        sc = self.scale
        
        exercise_w = int(BASE_W * sc)
        exercise_h = int(EXEC_H * sc)
        
        # Redimensionnement vers l'écran d'exercice ancré par le bas droit
        new_x = self.fixed_right - exercise_w
        new_y = self.fixed_bottom - exercise_h
        self.root.geometry(f"{exercise_w}x{exercise_h}+{new_x}+{new_y}")

        self.canvas = tk.Canvas(self.container, width=exercise_w, height=exercise_h, highlightthickness=0, bg=BG_MAIN)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.bind("<Button-1>", self._on_canvas_click)

        horizon_y = int(exercise_h * 0.52)
        self._init_stars(exercise_w, horizon_y)
        self._init_rain(exercise_w, exercise_h)
        self._init_rain_ripples(exercise_w, horizon_y, exercise_h)
        self._init_fireflies(exercise_w, horizon_y, exercise_h)
        self.birds_fx = []

        self.running = True
        self.is_paused = False
        self.session_time_elapsed = 0.0
        self._last_tick_time = time.monotonic()
        self.cycle_count = 0
        self.phase = "inhale"
        self.phase_t = 0.0
        
        self._start_sound()
        self._tick()

    def _on_canvas_click(self, event):
        x, y = event.x, event.y
        sc = self.scale
        cw = int(BASE_W * sc)

        if 10 * sc <= x <= 45 * sc and 10 * sc <= y <= 45 * sc:
            self._stop_exercise_and_return()
            return

        if 45 * sc <= x <= 80 * sc and 10 * sc <= y <= 45 * sc:
            self._toggle_pause_live()
            return

        if (cw - 75 * sc) <= x <= (cw - 45 * sc) and 10 * sc <= y <= 45 * sc:
            self._toggle_mute_live()
            return

        if (cw - 45 * sc) <= x <= (cw - 10 * sc) and 10 * sc <= y <= 45 * sc:
            self._stop_exercise_and_return()
            self.root.destroy()

    def _toggle_pause_live(self):
        self.is_paused = not self.is_paused
        if self.is_paused:
            self._stop_sound()
        else:
            self._last_tick_time = time.monotonic()
            self._start_sound()
        dur = self._phase_duration()
        frac = self.phase_t / dur if dur > 0 else 0.0
        if self.phase == "inhale": progress = frac
        elif self.phase == "hold_full": progress = 1.0
        elif self.phase == "exhale": progress = 1.0 - frac
        else: progress = 0.0
        self._draw_scene(progress, self.phase)

    def _toggle_mute_live(self):
        self.is_muted = not self.is_muted
        if self.is_muted or self.is_paused:
            self._stop_sound()
        else:
            self._start_sound()

    def _stop_exercise_and_return(self):
        self.running = False
        if self._after_id:
            self.root.after_cancel(self._after_id)
        self._stop_sound()
        self._show_home_screen()

    def _show_goal_reached_screen(self):
        self._clear_container()
        sc = self.scale

        frame = tk.Frame(self.container, bg=BG_MAIN)
        frame.pack(expand=True, fill="both", padx=int(20*sc), pady=int(20*sc))

        lbl_goal = tk.Label(frame, text=self._get_txt("goal_reached"), font=("Segoe UI", int(max(16, int(22*sc))), "bold"), bg=BG_MAIN, fg=ACCENT)
        lbl_goal.pack(pady=(int(35*sc), int(25*sc)))

        btn_menu = tk.Button(
            frame, text=self._get_txt("btn_menu"), font=("Segoe UI", int(max(9, int(11*sc))), "bold"),
            bg=ACCENT, fg="white", relief="flat", activebackground=ACCENT_HOVER, activeforeground="white",
            bd=0, pady=int(8*sc), cursor="hand2", command=self._show_home_screen
        )
        btn_menu.pack(fill="x", pady=int(5*sc))
        self._bind_hover(btn_menu, ACCENT, ACCENT_HOVER)

        btn_quit = tk.Button(
            frame, text=self._get_txt("btn_quit"), font=("Segoe UI", int(max(9, int(11*sc)))),
            bg=BG_CARD, fg=TEXT_LIGHT, relief="flat", activebackground="#1e1845", activeforeground="white",
            bd=0, pady=int(8*sc), cursor="hand2", command=self.root.destroy
        )
        btn_quit.pack(fill="x", pady=int(5*sc))
        self._bind_hover(btn_quit, BG_CARD, "#1e1845")

    def _tick(self):
        if not self.running: return
        
        t_now = time.monotonic()
        dt = t_now - self._last_tick_time
        self._last_tick_time = t_now

        if not self.is_paused:
            self.phase_t += dt
            self.session_time_elapsed += dt
            dur = self._phase_duration()

            while self.phase_t >= dur and self.running:
                self.phase_t -= dur
                self._next_phase()
                dur = self._phase_duration()

        if not self.running: return
        dur = self._phase_duration()
        frac = self.phase_t / dur if dur > 0 else 0.0

        if self.phase == "inhale": progress = frac
        elif self.phase == "hold_full": progress = 1.0
        elif self.phase == "exhale": progress = 1.0 - frac
        else: progress = 0.0

        self._draw_scene(progress, self.phase)

        if self.selected_duration_id != "free" and not self.is_paused:
            target_min = 5 if self.selected_duration_id == "eq" else 2
            if self.session_time_elapsed >= (target_min * 60):
                self.running = False
                if self._after_id:
                    self.root.after_cancel(self._after_id)
                self._stop_sound()
                self._show_goal_reached_screen()
                return

        self._after_id = self.root.after(50, self._tick)

    def _phase_duration(self):
        m = MODES_KEYS[self.selected_mode_idx]
        cfg = {"inhale": m[1], "hold_full": m[2], "exhale": m[3], "hold_empty": m[4]}
        return cfg.get(self.phase, 1)

    def _next_phase(self):
        m = MODES_KEYS[self.selected_mode_idx]
        cfg = {"hold_full": m[2], "hold_empty": m[4]}
        if self.phase == "inhale":
            self.phase = "hold_full" if cfg["hold_full"] > 0 else "exhale"
        elif self.phase == "hold_full":
            self.phase = "exhale"
        elif self.phase == "exhale":
            if cfg["hold_empty"] > 0: self.phase = "hold_empty"
            else:
                self.phase = "inhale"
                self.cycle_count += 1
        elif self.phase == "hold_empty":
            self.phase = "inhale"
            self.cycle_count += 1

    def _draw_scene(self, progress: float, phase: str):
        c = self.canvas
        c.delete("all")
        sc = self.scale
        cw = int(BASE_W * sc)
        ch = int(EXEC_H * sc)
        horizon = int(ch * 0.52)
        
        if self.is_paused:
            t_now = getattr(self, '_paused_scene_time', time.monotonic())
            self._paused_scene_time = t_now
        else:
            t_now = time.monotonic()
            if hasattr(self, '_paused_scene_time'): delattr(self, '_paused_scene_time')

        is_nuit = (self.selected_sound_id == "night")
        eff_progress = 0.0 if is_nuit else progress

        rock_base = lerp_rgb(ROCK_DARK, lerp_rgb(ROCK_MID, (200, 140, 120), 0.3), eff_progress * 0.5)

        if is_nuit:
            col_top   = lerp_rgb(rock_base, (140, 155, 200), 0.08)
            col_left  = lerp_rgb(rock_base, (15, 10, 35), 0.2)
            col_right = lerp_rgb(rock_base, (160, 180, 220), 0.12)
            col_bot   = lerp_rgb(rock_base, (20, 15, 40), 0.25)
            rock_col_shadow = lerp_rgb((20, 10, 50), ROCK_DARK, 0.0)
        else:
            col_top   = lerp_rgb(rock_base, (240, 190, 170), progress * 0.25)
            col_left  = lerp_rgb(rock_base, (40, 25, 75), 0.15)
            col_right = lerp_rgb(rock_base, (255, 210, 180), progress * 0.15)
            col_bot   = lerp_rgb(rock_base, (30, 20, 60), 0.25)
            rock_col_shadow = lerp_rgb((20, 10, 50), ROCK_DARK, progress * 0.4)

        sky_top, sky_bot = sky_color(eff_progress)
        bands = 45
        for i in range(bands):
            t = i / bands
            col = lerp_rgb(sky_top, sky_bot, t)
            y0 = int(i * horizon / bands)
            y1 = int((i + 1) * horizon / bands)
            c.create_rectangle(0, y0, cw, y1 + 1, fill=rgb(*col), outline="")

        star_opacity = 1.0 if is_nuit else max(0.0, min(1.0, 1.0 - (progress * 1.5)))
        if star_opacity > 0.05:
            for sx, sy, size, brightness in self.stars:
                alpha_col = lerp_rgb(sky_color(eff_progress)[1], (255, 255, 255), brightness * star_opacity)
                c.create_rectangle(sx, sy, sx + size, sy + size, fill=rgb(*alpha_col), outline="")

        astro_r = int(26 * sc) if is_nuit else int(28 * sc)
        astro_cx = int(cw * 0.5) if is_nuit else int(cw * 0.52)
        astro_apex = astro_r + int(10 * sc)
        astro_hidden = horizon + astro_r + 2   
        astro_cy = int(lerp(astro_hidden, astro_apex, progress))

        if is_nuit:
            for hr in [astro_r + int(18 * sc), astro_r + int(9 * sc)]:
                fill_t = 0.06 if hr > astro_r + int(9 * sc) else 0.18
                c.create_oval(astro_cx - hr, astro_cy - hr, astro_cx + hr, astro_cy + hr, fill=rgb(*lerp_rgb(sky_bot, MOON_HALO, fill_t)), outline="")
            c.create_oval(astro_cx - astro_r, astro_cy - astro_r, astro_cx + astro_r, astro_cy + astro_r, fill=rgb(*MOON_INNER), outline="")
        else:
            target_halo_color = lerp_rgb(SUN_OUTER, SUN_MID, progress * 0.3)
            for hr in [astro_r + int(25 * sc), astro_r + int(14 * sc)]:
                fill_t = 0.15 if hr > astro_r + int(14 * sc) else 0.35
                c.create_oval(astro_cx - hr, astro_cy - hr, astro_cx + hr, astro_cy + hr, fill=rgb(*lerp_rgb(sky_bot, target_halo_color, fill_t)), outline="")
            for sr, scol in [(astro_r, SUN_MID), (int(astro_r * 0.65), SUN_INNER)]:
                c.create_oval(astro_cx - sr, astro_cy - sr, astro_cx + sr, astro_cy + sr, fill=rgb(*scol), outline="")

        if self.selected_sound_id == "birds":
            if not self.is_paused:
                self._update_birds_fx(cw, horizon)
            bird_color = rgb(35, 25, 65) if progress < 0.35 else rgb(55, 40, 90)
            for bird in self.birds_fx:
                bx, by = bird["x"], bird["y"]
                ws = int(3 * sc)
                wing_y = int(math.sin(bird["wing_state"]) * 1.5 * sc)
                c.create_line(bx - ws, by - wing_y, bx, by, fill=bird_color, width=1)
                c.create_line(bx, by, bx + ws, by - wing_y, fill=bird_color, width=1)

            perch_col = rgb(30, 20, 60) if progress < 0.35 else rgb(60, 45, 85)
            rock_defs = [(-0.026, 130, 90), (0.158, 70, 50), (0.789, 95, 55)]
            perch_targets = [(0, 0.45), (0, 0.60), (1, 0.50), (2, 0.35), (2, 0.55)]
            
            y_base_rock = horizon + int(32 * sc)
            for rock_idx, t_pos in perch_targets:
                rx_ratio, rw, rh = rock_defs[rock_idx]
                rx = int(cw * rx_ratio)
                px = rx + int(rw * sc * t_pos)
                py = y_base_rock - int(rh * sc * math.sin(math.pi * t_pos) * 0.9)
                
                head_bob = int(math.sin(t_now * 1.5 + px) * 0.6 * sc)
                ps = max(1, int(2 * sc))
                
                c.create_oval(px - ps, py - ps + head_bob, px + ps, py + ps + head_bob, fill=perch_col, outline="")
                hs = max(1, int(1.5 * sc))
                c.create_oval(px - hs, py - ps * 2 - hs + head_bob, px + hs, py - ps * 2 + hs + head_bob, fill=perch_col, outline="")

        w_col = water_color(eff_progress)
        water_bands = 50
        water_top = lerp_rgb(w_col, (20, 15, 45), 0.3)
        water_bot = lerp_rgb(w_col, (15, 10, 40), 0.4)
        for i in range(water_bands):
            t = i / water_bands
            col = lerp_rgb(water_top, water_bot, t)
            y0 = horizon + int(i * (ch - horizon) / water_bands)
            y1 = horizon + int((i + 1) * (ch - horizon) / water_bands) + 1
            c.create_rectangle(0, y0, cw, y1, fill=rgb(*col), outline="")

        if star_opacity > 0.1:
            for sx, sy, size, brightness in self.stars:
                dist_from_horizon = horizon - sy
                ry_base = horizon + dist_from_horizon
                if horizon < ry_base < ch:
                    depth_factor = 1.0 - ((ry_base - horizon) / (ch - horizon))
                    ref_alpha = brightness * star_opacity * depth_factor * 0.6
                    wave_mod = math.sin(ry_base * 0.7 + t_now * 2) * 2 * (1.0 - depth_factor)
                    rx = sx + int(wave_mod)
                    ref_col = lerp_rgb(water_top, (240, 240, 255), ref_alpha)
                    c.create_rectangle(rx, ry_base, rx + size, ry_base + 1, fill=rgb(*ref_col), outline="")

        if progress > 0.001 and astro_cy < horizon + astro_r:
            water_h = ch - horizon
            w_top, w_bot = int(int(astro_r * 1.3) * progress), int(int(cw * 0.35) * progress)
            for i in range(water_h):
                t_y = i / water_h
                y_curr = horizon + i
                current_w = int(lerp(w_top, w_bot, t_y))
                if current_w > 0:
                    if is_nuit:
                        color_refl = lerp_rgb(w_col, MOON_INNER, (1.0 - (t_y * 0.75)) * 0.45 * progress)
                    else:
                        color_refl = lerp_rgb(w_col, lerp_rgb(SUN_OUTER, SUN_INNER, progress), (1.0 - (t_y * 0.7)) * 0.85)
                    wave_mod = math.sin(y_curr * 0.8 + t_now * 4) * 4 * (1.0 - t_y) * progress
                    c.create_line(int(astro_cx - current_w + wave_mod), y_curr, int(astro_cx + current_w - wave_mod), y_curr, fill=rgb(*color_refl), width=1)

        if self.selected_sound_id == "rain":
            if not self.is_paused:
                self._update_rain_ripples(cw, horizon, ch)
            for ripple in self.rain_ripples:
                alpha_factor = math.sin(ripple["life"])
                base_ripple_rgb = (235, 240, 255) if progress > 0.4 else (130, 120, 180)
                ripple_col = lerp_rgb(water_color(progress), base_ripple_rgb, alpha_factor * 0.4)
                c.create_line(ripple["x"], ripple["y"], ripple["x"] + ripple["len"], ripple["y"], fill=rgb(*ripple_col), width=1)

        if self.selected_sound_id == "sea":
            wave_configs = [
                {"y_offset": 15, "freq": 0.04, "amp": 3, "speed": 3.0, "color": (245, 248, 255), "alpha": 0.25}, 
                {"y_offset": 45, "freq": 0.02, "amp": 5, "speed": -2.0, "color": (255, 255, 255), "alpha": 0.35}, 
                {"y_offset": 80, "freq": 0.015, "amp": 6, "speed": 1.5, "color": (140, 110, 180), "alpha": 0.2} 
            ]
            for config in wave_configs:
                pts = []
                y_base_wave = horizon + int(config["y_offset"] * sc)
                if y_base_wave < ch - 10:
                    for x in range(0, cw + 10, 10):
                        y_wave = y_base_wave + int(config["amp"] * sc * math.sin(x * config["freq"] + t_now * config["speed"]))
                        pts.append((x, y_wave))
                    v_color = lerp_rgb(water_color(progress), config["color"], config["alpha"])
                    for idx in range(len(pts) - 1):
                        c.create_line(pts[idx][0], pts[idx][1], pts[idx+1][0], pts[idx+1][1], fill=rgb(*v_color), width=max(1, int(1.5 * sc)))

        lily_col = lerp_rgb(LILY_COLOR, (120, 80, 160), eff_progress * 0.3)
        lily_data = [(int(cw*0.22), 13, 0.65), (int(cw*0.78), 11, 0.65), (int(cw*0.31), 8, 0.65)]
        
        for lx, lr, y_ratio in lily_data:
            ly = horizon + int((ch - horizon) * y_ratio)
            r_sc = int(lr * sc)
            if self.selected_sound_id == "sea":
                ly += int(2.5 * sc * math.sin(lx * 0.02 + t_now * 2.0))
                pitch_mod = 0.35 + 0.08 * math.cos(lx * 0.05 + t_now * 2.5)
            else:
                pitch_mod = 0.35
            c.create_oval(lx - r_sc, ly - int(r_sc * pitch_mod), lx + r_sc, ly + int(r_sc * pitch_mod), fill=rgb(*lily_col), outline="")

        for rx_ratio, rw, rh in [(-0.026, 130, 90), (0.158, 70, 50), (0.789, 95, 55)]:
            rx = int(cw * rx_ratio)
            y_base = horizon + int(32 * sc)
            shadow_h = int(rh * sc * 0.25)
            c.create_oval(rx + int(rw*sc*0.02), y_base - shadow_h, rx + int(rw*sc*0.98), y_base + shadow_h, fill=rgb(*rock_col_shadow), outline="")
            
            contour_pts = []
            steps = 12
            for i in range(steps + 1):
                t = i / steps
                px = rx + int(rw * sc * t)
                py = y_base - int(rh * sc * math.sin(math.pi * t) * 0.9)
                contour_pts.append((px, py))

            apex_x = rx + int(rw * sc * 0.52)
            apex_y = y_base - int(rh * sc * 0.55)
            mid_left, mid_right = steps // 4, (3 * steps) // 4

            poly_left = [contour_pts[0][0], contour_pts[0][1]]
            for i in range(1, mid_left + 1): poly_left.extend([contour_pts[i][0], contour_pts[i][1]])
            poly_left.extend([apex_x, apex_y, rx, y_base])
            c.create_polygon(poly_left, fill=rgb(*col_left), outline="")

            poly_top = [apex_x, apex_y]
            for i in range(mid_left, mid_right + 1): poly_top.extend([contour_pts[i][0], contour_pts[i][1]])
            c.create_polygon(poly_top, fill=rgb(*col_top), outline="")

            poly_right = [apex_x, apex_y]
            for i in range(mid_right, steps + 1): poly_right.extend([contour_pts[i][0], contour_pts[i][1]])
            poly_right.extend([rx + int(rw * sc), y_base])
            c.create_polygon(poly_right, fill=rgb(*col_right), outline="")

            poly_bot = [contour_pts[0][0], contour_pts[0][1], apex_x, apex_y, contour_pts[steps][0], contour_pts[steps][1], rx, y_base]
            c.create_polygon(poly_bot, fill=rgb(*col_bot), outline="")

        reed_col, oran_col = lerp_rgb(REED_DARK, (100, 60, 120), eff_progress * 0.3), lerp_rgb(REED_ORANGE, (230, 150, 80), eff_progress * 0.3)
        for rx_ratio, num_r in [(0.047, 6), (0.842, 5)]:
            rx_grp = int(cw * rx_ratio)
            for i in range(num_r):
                sx = rx_grp + int((i * 9 + (i % 3) * 3) * sc)
                height = int((55 + (i % 3) * 18) * sc)
                wind_noise = math.sin(t_now * 1.8 + i * 0.5) * 2.2 + math.cos(t_now * 3.1 + i * 1.2) * 0.8
                wind_offset = wind_noise * sc
                top_x = sx + int(wind_offset * (1.1 + (i % 2) * 0.3))
                
                c.create_line(top_x, horizon + height, sx, ch, fill=rgb(*reed_col), width=max(1, int(2 * sc)))
                c.create_line(top_x, horizon + height - int(10*sc), top_x + int((12 + (i%2)*6)*sc) + int(wind_offset*0.3), horizon + height - int(30*sc), fill=rgb(*reed_col), width=1)
                c.create_rectangle(top_x - int(3*sc), horizon + height - int((18 + (i % 2) * 6) * sc), top_x + int(3*sc), horizon + height, fill=rgb(*oran_col), outline="")

        if is_nuit:
            if not self.is_paused:
                self._update_fireflies(cw, horizon, ch)
            for f in self.fireflies:
                glow_mod = (math.sin(f["phase"]) + 1.0) / 2.0
                if glow_mod > 0.25:
                    fx, fy = int(f["x"]), int(f["y"])
                    g_r = int(lerp(160, 210, glow_mod))
                    g_g = int(lerp(235, 255, glow_mod))
                    g_b = int(lerp(40, 100, glow_mod))
                    f_color = rgb(g_r, g_g, g_b)

                    hr = int(max(3, 5 * glow_mod * sc))
                    c.create_oval(fx - hr, fy - hr, fx + hr, fy + hr, fill=rgb(*lerp_rgb(water_color(0.0), (g_r, g_g, g_b), 0.22 * glow_mod)), outline="")
                    c.create_oval(fx - 1, fy - 1, fx + 2, fy + 2, fill=f_color, outline="")

        lbl_inst = {"inhale": self._get_txt("phase_in"), "hold_full": self._get_txt("phase_hold_f"), "exhale": self._get_txt("phase_out"), "hold_empty": self._get_txt("phase_hold_e")}.get(phase, "")
        rem = max(0, self._phase_duration() - self.phase_t)
        
        if self.is_paused:
            c.create_text(cw//2, ch - int(45*sc), text="PAUSE", fill="#ffdd6b", font=("Segoe UI", int(max(10, int(14 * sc))), "bold"))
        else:
            c.create_text(cw//2, ch - int(45*sc), text=f"{lbl_inst}  {math.ceil(rem)}s", fill="white", font=("Segoe UI", int(max(9, int(13 * sc))), "bold"))
        
        tot_label = self._get_txt("dur_eq").split(" - ")[0] if self.selected_duration_id == "eq" else (self._get_txt("dur_stress").split(" - ")[0] if self.selected_duration_id == "stress" else "∞")
        info_txt = f"{self._get_txt('cycle')} {self.cycle_count}  —  {int(self.session_time_elapsed // 60)}:{int(self.session_time_elapsed % 60):02d} / {tot_label}"
        c.create_text(cw//2, ch - int(20*sc), text=info_txt, fill="white", font=("Segoe UI", int(max(7, int(9 * sc)))))

        c.create_text(int(25*sc), int(25*sc), text="🏠", fill="#51aef2", font=("Segoe UI", int(max(12, int(16*sc))), "bold"))
        play_pause_icon = "▶" if self.is_paused else "⏸"
        c.create_text(int(60*sc), int(25*sc), text=play_pause_icon, fill="#51aef2", font=("Segoe UI", int(max(11, int(15*sc))), "bold"))
        mute_icon = "🔇" if self.is_muted else "🔊"
        c.create_text(cw - int(60*sc), int(24*sc), text=mute_icon, fill="#51aef2", font=("Segoe UI", int(max(11, int(15*sc))), "bold"))
        c.create_text(cw - int(22*sc), int(24*sc), text="✕", fill="#51aef2", font=("Segoe UI", int(max(10, int(14*sc))), "bold"))

        if self.selected_sound_id == "rain":
            if not self.is_paused:
                self._update_rain(cw, ch)
            rain_color = rgb(150, 160, 220)
            for drop in self.rain_drops:
                c.create_line(drop["x"], drop["y"], drop["x"] + (drop["len"] * 0.15), drop["y"] + drop["len"], fill=rain_color, width=1)

    def _start_sound(self):
        if self.is_muted or self.is_paused: return  
        self._sound_stop.clear()
        self._sound_thread = threading.Thread(target=self._sound_loop, args=(self.selected_sound_id,), daemon=True)
        self._sound_thread.start()

    def _stop_sound(self):
        self._sound_stop.set()
        try: winsound.PlaySound(None, winsound.SND_PURGE)
        except Exception: pass

    def _sound_loop(self, choice):
        try:
            sound_mapping = {"sea": "mer.wav", "birds": "oiseaux.wav", "rain": "pluie.wav", "night": "grillons.wav"}
            if choice not in sound_mapping: return
            
            if getattr(sys, 'frozen', False):
                base_dir = sys._MEIPASS
            else:
                base_dir = os.path.dirname(os.path.abspath(__file__))
                
            full_path = os.path.join(base_dir, sound_mapping[choice])
            if not os.path.exists(full_path): return

            winsound.PlaySound(full_path, winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
            while not self._sound_stop.is_set():
                time.sleep(0.2)
        except Exception: pass

    def _drag_start(self, e):
        self._dx, self._dy = e.x, e.y

    def _drag_move(self, e):
        # Permet de déplacer l'application, tout en mettant à jour le repère fixe bas-droit
        x = self.root.winfo_x() + e.x - self._dx
        y = self.root.winfo_y() + e.y - self._dy
        self.root.geometry(f"+{x}+{y}")
        self.fixed_right = x + self.w
        self.fixed_bottom = y + self.h


if __name__ == "__main__":
    root = tk.Tk()
    root.title("AUROR Breath")
    app = CoherenceApp(root)
    root.mainloop()