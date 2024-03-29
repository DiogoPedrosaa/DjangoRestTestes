$(document).ready(function() {
    var isSortedAsc = false;

    // Adicione um botão de ordenação ao lado das colunas desejadas
    $('.sortable').append('<span class="sort-icon">&#x25B2;</span>');

    $('.sortable').on('click', function() {
        var index = $(this).index();
        var rows = $('tbody tr').get();

        rows.sort(function(a, b) {
            var aValue = $(a).children('td').eq(index).text();
            var bValue = $(b).children('td').eq(index).text();

            // Converte os valores para números antes de comparar
            aValue = parseInt(aValue) || 0;
            bValue = parseInt(bValue) || 0;

            return isSortedAsc ? aValue - bValue : bValue - aValue;
        });

        $.each(rows, function(index, row) {
            $('tbody').append(row);
        });

        isSortedAsc = !isSortedAsc;

        // Atualiza a aparência do ícone de ordenação
        $('.sortable .sort-icon').html(isSortedAsc ? '&#x25BC;' : '&#x25B2;');
    });
});

$(document).ready(function() {
    $('#filtroClasse').on('change', function() {
        var selectedClass = $(this).val();
        filterTableByClass(selectedClass);
    });

    function filterTableByClass(selectedClass) {
        // Esconda todas as linhas da tabela
        $('tbody tr').hide();

        // Mostre apenas as linhas que correspondem à classe selecionada
        if (selectedClass === "") {
            $('tbody tr').show();
        } else {
            $('tbody tr td:nth-child(4)').filter(':contains("' + selectedClass + '")').parent().show();
        }
    }
});