#!/usr/bin/env python3
"""
show_nexus.py
Small tkinter app to display Nexus Infinity interview and production-sector report.
Run: python3 show_nexus.py
"""
import tkinter as tk
from tkinter import ttk
import json
import os
from tkinter import messagebox

COMPANY_INFO = {
    "name": "Nexus Infinity",
    "area": "Jogos e brinquedos",
    "product": "Fazer brinquedos e jogos com produtos recicláveis, criando jogos envolventes e inovadores que proporcionem experiências únicas, despertem emoções e conectem pessoas, transformando ideias em diversão e qualidade.",
    "audience": "Pessoas acima dos oito anos",
    "brief": (
        "Nexus Infinity quer reunir jogos, reciclagem e valores. Missão: criar brinquedos e jogos recicláveis que ofereçam experiências únicas,\n"
        "despertem emoções e conectem pessoas. Visão: ser referência global em criatividade, qualidade e impacto positivo."
    )
}

MARKETING_REPORT = {
    "owner": "Thomas (dono)",
    "manager": "Arthur (gerente do marketing)",
    "submanager": "Maria (subgerente)",
    "company": "Nexus Infinity",
    "area": "Marketing",
    "product": "Fazer brinquedos e jogos com produtos recicláveis",
    "audience": "Pessoas de todas as idades",
    "description": (
        "Compreender a visão do proprietário sobre o funcionamento da empresa, a eficiência dos setores,\n"
        "os desafios enfrentados e as perspectivas futuras do negócio."
    )
}

MARKETING_HELP = (
    "Função geral do Marketing:\n"
    "- Desenvolver identidade visual e designs dos brinquedos e materiais de divulgação.\n"
    "- Divulgar a empresa e atrair clientes; auxiliar na apresentação do produto.\n"
    "Problema citado por Ellen: Atraso na entrega dos designs, que atrasou a Produção.\n"
    'Comentário de Ellen: "Eu tive um pouco de problema com o Marketing porque eles não estavam entregando o design no prazo."'
)

HISTORY_ROWS = [
    ("22/06/2026", "Marketing", "Análise das redes sociais da empresa"),
    ("22/06/2026", "Financeiro", "Levantamento dos possíveis custos"),
    ("22/06/2026", "Produção", "Estudo do processo de entrega do produto"),
    ("22/06/2026", "RH", "Análise da organização das funções")
]

INTERVIEWERS = ("Maria de Alencar", "Amanda")


def make_label(frame, text, **kwargs):
    lbl = tk.Label(frame, text=text, justify=tk.LEFT, anchor='w', **kwargs)
    return lbl


def show_interviewers(root):
    w = tk.Toplevel(root)
    w.title("Entrevistadores - Nexus Infinity")
    w.geometry("700x400")

    header = tk.Frame(w)
    header.pack(fill='x', padx=12, pady=8)
    tk.Label(header, text=COMPANY_INFO['name'], font=(None, 20, 'bold')).pack(anchor='w')
    tk.Label(header, text=f"Entrevistadores: {', '.join(INTERVIEWERS)}", font=(None, 12)).pack(anchor='w')

    body = tk.Frame(w)
    body.pack(fill='both', expand=True, padx=12, pady=6)
    txt = tk.Text(body, wrap='word', height=12)
    txt.insert('end', f"Área de atuação: {COMPANY_INFO['area']}\n\n")
    txt.insert('end', f"Produto/serviço principal: {COMPANY_INFO['product']}\n\n")
    txt.insert('end', f"Público-alvo: {COMPANY_INFO['audience']}\n\n")
    txt.insert('end', f"Descrição: {COMPANY_INFO['brief']}\n")
    txt.configure(state='disabled')
    txt.pack(fill='both', expand=True)


def show_marketing_report(root):
    w = tk.Toplevel(root)
    w.title("Relatório - Setor de Marketing")
    w.geometry("900x700")

    header = tk.Frame(w)
    header.pack(fill='x', padx=12, pady=8)
    tk.Label(header, text=f"Relatório do Setor de Marketing - {MARKETING_REPORT['company']}", font=(None, 18, 'bold')).pack(anchor='w')

    info = tk.Frame(w)
    info.pack(fill='x', padx=12, pady=6)
    make_label(info, f"Dono da empresa: {MARKETING_REPORT['owner']}", font=(None, 11)).pack(anchor='w')
    make_label(info, f"Gerente do Marketing: {MARKETING_REPORT['manager']}", font=(None, 11)).pack(anchor='w')
    make_label(info, f"Subgerente: {MARKETING_REPORT['submanager']}", font=(None, 11)).pack(anchor='w')
    make_label(info, f"Área: {MARKETING_REPORT['area']}", font=(None, 11)).pack(anchor='w')
    make_label(info, f"Produto/serviço principal: {MARKETING_REPORT['product']}", font=(None, 11)).pack(anchor='w')
    make_label(info, f"Público-alvo: {MARKETING_REPORT['audience']}", font=(None, 11)).pack(anchor='w')

    desc_frame = tk.LabelFrame(w, text='Breve descrição')
    desc_frame.pack(fill='both', expand=False, padx=12, pady=8)
    tk.Label(desc_frame, text=MARKETING_REPORT['description'], justify='left', wraplength=840).pack(anchor='w', padx=6, pady=6)

    # Notes area: entrevista e observações (editáveis)
    notes_frame = tk.LabelFrame(w, text='Entrevista e Observações (edite abaixo)')
    notes_frame.pack(fill='both', expand=True, padx=12, pady=8)

    left = tk.Frame(notes_frame)
    left.pack(side='left', fill='both', expand=True, padx=(6,3), pady=6)
    tk.Label(left, text='Entrevista realizada (quem entrevistou: Maria de Alencar, Amanda):', anchor='w', justify='left').pack(anchor='w')
    interview_text = tk.Text(left, wrap='word', height=10)
    interview_text.pack(fill='both', expand=True, pady=(4,6))

    right = tk.Frame(notes_frame)
    right.pack(side='right', fill='both', expand=True, padx=(3,6), pady=6)
    tk.Label(right, text='Observações sobre o Marketing:', anchor='w', justify='left').pack(anchor='w')
    observations_text = tk.Text(right, wrap='word', height=10)
    observations_text.pack(fill='both', expand=True, pady=(4,6))

    # helper functions to save/load notes to a local JSON file
    notes_file = os.path.join(os.path.dirname(__file__), 'marketing_notes.json')

    def load_notes():
        if os.path.exists(notes_file):
            try:
                with open(notes_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                interview_text.delete('1.0', 'end')
                observations_text.delete('1.0', 'end')
                interview_text.insert('end', data.get('interview', ''))
                observations_text.insert('end', data.get('observations', ''))
            except Exception as e:
                messagebox.showwarning('Erro', f'Erro ao carregar notas: {e}')

    def save_notes():
        data = {
            'interview': interview_text.get('1.0', 'end').strip(),
            'observations': observations_text.get('1.0', 'end').strip()
        }
        try:
            with open(notes_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            messagebox.showinfo('Salvo', f'Notas salvas em: {notes_file}')
            update_saved_display()
        except Exception as e:
            messagebox.showerror('Erro', f'Falha ao salvar: {e}')

    btns = tk.Frame(w)
    btns.pack(fill='x', padx=12, pady=(0,8))
    tk.Button(btns, text='Carregar notas existentes', command=load_notes, width=20).pack(side='left', padx=6)
    tk.Button(btns, text='Salvar notas', command=save_notes, width=14).pack(side='left', padx=6)

    # Display saved notes below for quick review
    saved_frame = tk.LabelFrame(w, text='Notas salvas (visualização)')
    saved_frame.pack(fill='both', expand=False, padx=12, pady=6)
    saved_label = tk.Label(saved_frame, text='', justify='left', anchor='w', wraplength=840)
    saved_label.pack(fill='both', expand=True, padx=6, pady=6)

    def update_saved_display():
        if os.path.exists(notes_file):
            try:
                with open(notes_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                text = f"Entrevista:\n{data.get('interview','')}\n\nObservações:\n{data.get('observations','')}"
                saved_label.config(text=text)
            except Exception as e:
                saved_label.config(text=f'Erro ao ler arquivo: {e}')
        else:
            saved_label.config(text='Nenhuma nota salva ainda.')

    # load any existing notes on opening
    load_notes()
    update_saved_display()

    # histórico e conclusão (mantidos)
    hist_frame = tk.LabelFrame(w, text='Histórico da análise')
    hist_frame.pack(fill='both', expand=True, padx=12, pady=8)

    cols = ('date', 'sector', 'desc')
    tree = ttk.Treeview(hist_frame, columns=cols, show='headings', height=6)
    tree.heading('date', text='Data')
    tree.heading('sector', text='Setor')
    tree.heading('desc', text='Descrição')
    tree.column('date', width=100)
    tree.column('sector', width=120)
    tree.column('desc', width=520)
    for r in HISTORY_ROWS:
        tree.insert('', 'end', values=r)
    tree.pack(fill='both', expand=True, padx=6, pady=6)

    concl_frame = tk.LabelFrame(w, text='Conclusão da equipe')
    concl_frame.pack(fill='both', expand=False, padx=12, pady=8)
    conclusion = (
        "Concluímos que o setor de Marketing é essencial para divulgar e posicionar os produtos.\n"
        "Principal problema observado: atrasos na entrega dos designs, que impactam Produção.\n"
        "Melhoria prioritária: melhorar o cronograma entre Marketing e Produção, e criar checklists para entrega de designs."
    )
    tk.Label(concl_frame, text=conclusion, justify='left', wraplength=840).pack(anchor='w', padx=6, pady=6)


def main():
    root = tk.Tk()
    root.title('Nexus Infinity - Painel')
    root.geometry('640x320')

    style = ttk.Style()
    try:
        style.theme_use('clam')
    except Exception:
        pass

    header = tk.Frame(root)
    header.pack(fill='x', pady=(12,6))
    tk.Label(header, text='Nexus Infinity', font=(None, 22, 'bold')).pack()
    tk.Label(header, text=f"Entrevistadores: {', '.join(INTERVIEWERS)}", font=(None, 10)).pack()

    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=18)
    tk.Button(btn_frame, text='Mostrar entrevistadores e apresentação', width=36, command=lambda: show_interviewers(root)).grid(row=0, column=0, padx=8, pady=6)
    tk.Button(btn_frame, text='Relatório do Setor de Marketing', width=36, command=lambda: show_marketing_report(root)).grid(row=1, column=0, padx=8, pady=6)

    footer = tk.Frame(root)
    footer.pack(side='bottom', fill='x', pady=8)
    tk.Label(footer, text='Clique em Relatório do Setor de Marketing para abrir a tela com edição de entrevistas e observações.', font=(None, 9), fg='gray').pack()

    root.mainloop()

if __name__ == '__main__':
    main()
