$(document).ready(function() {
    var isSortedAsc = false;

    $('.sortable').append('<span class="sort-icon">&#x25B2;</span>');

    $('.sortable').on('click', function() {
        var index = $(this).index();
        var rows = $('tbody tr').get();

        rows.sort(function(a, b) {
            var aValue = $(a).children('td').eq(index).text();
            var bValue = $(b).children('td').eq(index).text();

            aValue = parseInt(aValue) || 0;
            bValue = parseInt(bValue) || 0;

            return isSortedAsc ? aValue - bValue : bValue - aValue;
        });

        $.each(rows, function(index, row) {
            $('tbody').append(row);
        });

        isSortedAsc = !isSortedAsc;

        $('.sortable .sort-icon').html(isSortedAsc ? '&#x25BC;' : '&#x25B2;');
    });

    $('#filtroClasse').on('change', function() {
        var selectedClass = $(this).val();
        fetchCharactersByClass(selectedClass);
    });

    function fetchCharactersByClass(charClass) {
        var url = '/apis/characters/search-by-class/?class=' + charClass;

        $.ajax({
            url: url,
            method: 'GET',
            success: function(data) {
                updateTable(data);
            },
            error: function(error) {
                console.error('Error fetching characters:', error);
            }
        });
    }

    function updateTable(characters) {
        var tbody = $('tbody');
        tbody.empty();

        characters.forEach(function(character) {
            var row = `
                <tr>
                    <td>${character.char_nick}</td>
                    <td>${character.char_legacy_level}</td>
                    <td>${character.char_effect_level}</td>
                    <td>${character.char_class}</td>
                    <td><a href="${character.char_build}" class="build-button" target="_blank">Ver Build</a></td>
                </tr>
            `;
            tbody.append(row);
        });
    }
});
