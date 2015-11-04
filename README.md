# InstrumentID
Software web para identificação de instrumentos musicais pela transformada de wavelets.

Implementação do trabalho [documentado](https://github.com/yurifidelis/ArtigoAnaliseAudio) para o Trabalho de Conclusão de Curso, de Análise e Desenvolvimento de Sistemas do IFSP, campus Campos do Jordão.

O intuito deste projeto é implementar uma interface web para a visualização de arquivos de música de uma biblioteca criada pelo usuário. Todos os arquivos subidos são então análisados por algoritmos em Python que extraem features de MFCCs do arquivo subido. A partir da análise são feitas marcações dos tempos de introdução e fim das classes de instrumentos musicais identificados na música pela previsão de um classificador SVM. Essas marcações são apresentadas na interface sobrepostas à forma de onda do arquivo. O usuário pode usar as características identificadas para filtrar a lista de arquivos.
