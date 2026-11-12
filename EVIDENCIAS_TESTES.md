# Evidências dos Testes e Correções — PIT II

**Aluno:** Pedro Venicio Pereira da Silva Uchôa  
**RGM:** 33332541  
**Projeto:** Aplicativo de vendas online para loja de cupcakes gourmet

## 1. Mensagem de confirmação do carrinho
**Problema identificado:** a mensagem apresentada após adicionar um produto tinha pouco destaque visual.

**Correção aplicada:** foram criadas mensagens específicas para sucesso e erro, com maior contraste e texto mais claro.

**Evidência:** classes `msg ok` e `msg erro` e função `mensagem()` adicionadas ao arquivo `index.html`.

## 2. Validação dos campos obrigatórios
**Problema identificado:** quando faltavam dados, a orientação ao usuário era pouco específica.

**Correção aplicada:** o sistema passou a verificar nome, telefone, endereço, forma de pagamento e modalidade de entrega, informando exatamente quais campos precisam ser preenchidos.

**Evidência:** nova lógica de validação adicionada ao evento de finalização do formulário.

## 3. Acompanhamento do pedido
**Problema identificado:** as etapas de acompanhamento não indicavam com clareza a etapa atual.

**Correção aplicada:** a etapa “Pedido recebido” passou a receber maior destaque visual e a identificação “atual”, mantendo visíveis as demais fases: Pagamento confirmado, Em preparo, Em entrega e Concluído.

**Evidência:** atualização do componente de status no `index.html`.

## 4. Responsividade em telas menores
**Problema identificado:** alguns campos, botões e elementos do formulário ficavam muito próximos em telas reduzidas.

**Correção aplicada:** foram aumentados os espaçamentos entre os campos, as áreas de toque e a organização dos elementos do carrinho e do acompanhamento.

**Evidência:** regras adicionais adicionadas ao media query para telas de até 600 pixels.

## 5. Confirmação final do pedido
**Problema identificado:** a confirmação final apresentava poucas informações sobre o pedido.

**Correção aplicada:** foi incluído um resumo com número do pedido, nome do cliente, forma de pagamento, modalidade de entrega e status atual.

**Evidência:** novo bloco `confirmacao` inserido no arquivo `index.html`.

## Resultado da nova verificação
Após as correções, foram novamente verificados catálogo, carrinho, mensagens, validação dos campos, formas de pagamento, modalidades de entrega, acompanhamento, confirmação e adaptação para telas menores. O fluxo principal apresentou funcionamento satisfatório e maior clareza para o usuário.

## Funcionalidades previstas para evolução futura
- cadastro e login de usuários;
- pagamento real integrado;
- rastreamento da entrega em tempo real;
- histórico de pedidos;
- área administrativa para gerenciamento das vendas;
- testes em maior variedade de dispositivos e navegadores.
