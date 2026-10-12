import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Gestão Financeira Pessoal - Q4 2026",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .main-header { font-size: 24px; font-weight: bold; color: #1f77b4; }
    .card { background-color: #f8f9fa; padding: 20px; border-radius: 10px; border-left: 5px solid #1f77b4; margin-bottom: 10px; }
    .alert-card { background-color: #fff3cd; padding: 15px; border-radius: 8px; border-left: 5px solid #ffc107; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-header">💼 Painel Executivo de Controle Financeiro & Tesouraria (Q4 2026)</p>', unsafe_allow_html=True)

# 1. SIDEBAR: ATIVOS BASE
st.sidebar.header("⚙️ Configurações & Ativos Base")
st.sidebar.metric("Reserva em Espécie (Fixo)", "R$ 1.550,00")
st.sidebar.metric("Receita Fixa INSS (2º dia útil)", "R$ 1.576,91")
st.sidebar.metric("Teto de Crédito Contratado", "R$ 66.059,04")

# 2. DIÁRIO DE LANÇAMENTOS
st.subheader("📅 Diário de Lançamentos e Movimentações")
diario_data = [
    {"Data": "04/10/2026", "Descrição": "Configuração inicial e painel de limites globais", "Valor": "R$ 66.059,04 (Teto)"},
    {"Data": "05/10/2026", "Descrição": "Inclusão da Reserva em Espécie", "Valor": "R$ 1.550,00"},
    {"Data": "06/10/2026", "Descrição": "Abatimento Pix (IPTV R$ 13,00 + PicPay R$ 110,00)", "Valor": "-R$ 123,00"},
    {"Data": "11/10/2026", "Descrição": "Acréscimo no cartão Bradesco Amazon", "Valor": "+R$ 29,56"},
    {"Data": "18/10/2026", "Descrição": "[Lembrete] Pagamento da IPTV", "Valor": "R$ 35,00"},
    {"Data": "Recorrente", "Descrição": "Crédito Automático INSS (2º dia útil)", "Valor": "R$ 1.576,91"}
]
st.dataframe(pd.DataFrame(diario_data), use_container_width=True)

# 3. CHECKLIST DE NOVEMBRO
st.subheader("✅ Checklist de Pagamentos — Novembro / 2026 (Mês de Pico)")
st.info("Marque as despesas abaixo conforme efetuar os pagamentos para auditar o fluxo real.")

col1, col2, col3 = st.columns(3)
with col1:
    p_magalu = st.checkbox("Cartão Magazine Luiza (R$ 389,45)")
    p_amazon = st.checkbox("Bradesco Amazon (R$ 330,40)")
    p_bv = st.checkbox("Cartão BV (R$ 225,87)")
    p_nubank = st.checkbox("Nubank / NuPay (R$ 221,29)")
with col2:
    p_santander = st.checkbox("Santander (R$ 173,60)")
    p_c6 = st.checkbox("C6 Bank (R$ 108,86)")
    p_credicard = st.checkbox("Credicard On (R$ 105,04)")
    p_infinite = st.checkbox("Infinite Pay (R$ 90,98)")
with col3:
    p_caixa = st.checkbox("Cartão Caixa (R$ 62,50)")
    p_tim = st.checkbox("Conta TIM (R$ 43,00)")
    p_samsung = st.checkbox("Cartão Samsung (R$ 35,16)")
    p_iptv = st.checkbox("IPTV (R$ 35,00)")
    p_itau = st.checkbox("Cartão Múltiplo Itaú (R$ 33,23)")

despesas_nov = [
    (389.45, p_magalu), (330.40, p_amazon), (225.87, p_bv), (221.29, p_nubank),
    (173.60, p_santander), (108.86, p_c6), (105.04, p_credicard), (90.98, p_infinite),
    (62.50, p_caixa), (43.00, p_tim), (35.16, p_samsung), (35.00, p_iptv), (33.23, p_itau)
]

total_comprometido_nov = sum([d[0] for d in despesas_nov])
total_pago_nov = sum([d[0] for d in despesas_nov if d[1]])
total_pendente_nov = total_comprometido_nov - total_pago_nov

st.metric(label="Status do Mês de Novembro", value=f"Comprometido: R$ {total_comprometido_nov:.2f}", delta=f"Pago: R$ {total_pago_nov:.2f} | Pendente: R$ {total_pendente_nov:.2f}")

# 4. TABELA CONSOLIDADA DE FLUXO DE CAIXA
st.subheader("📊 Tabela Consolidada de Fluxo de Caixa (Q4 2026)")
tabela_fluxo = {
    "Categoria / Mês": [
        "Saldo Bancário Inicial (Banrisul)", 
        "Reserva em Espécie (Dinheiro Físico)", 
        "Receita Líquida INSS (2º dia útil)", 
        "Caixa Total Disponível", 
        "Total de Despesas do Mês", 
        "SALDO LÍQUIDO TRANSPORTADO"
    ],
    "Outubro / 2026": [
        "R$ 134,44", "R$ 1.550,00", "R$ 0,00", "R$ 1.684,44", "R$ 123,00", "R$ 1.561,44"
    ],
    "Novembro / 2026 (Pico)": [
        "R$ 1.561,44", "R$ 1.550,00", "R$ 1.576,91", "R$ 4.688,35", f"R$ {total_comprometido_nov:.2f}", "R$ 1.265,26"
    ],
    "Dezembro / 2026 (Descompressão)": [
        "R$ 1.265,26", "R$ 1.550,00", "R$ 1.576,91", "R$ 4.392,17", "R$ 1.017,36", "R$ 3.374,81"
    ]
}
st.dataframe(pd.DataFrame(tabela_fluxo), use_container_width=True)

