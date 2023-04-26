$(document).ready(function () {
    setInterval(reset_table, 1000);
    function reset_table() {
        if ($('#results_table').length) {
            if (!$("#results_table").hasClass("dataTable")) {
                $("#results_table").DataTable({
                    "language": {
                        "search": "جست و جو : ",
                        "lengthMenu": "نمایش _MENU_ در هر صفحه",
                        "zeroRecords": "رکوردی یافت نشد",
                        "info": "صفحه _PAGE_ از _PAGES_",
                        "infoEmpty": "رکوردی یافت نشد",
                        "infoFiltered": "(فیلتر شده از _MAX_ رکورد)",
                        "paginate": {
                            "previous": "قبلی",
                            "next": "بعدی",
                        }
                    }
                });
            }
        }
    }
});