$(document).ready(function () {
  $("#summernote").summernote({
    minHeight: 300,
    toolbar: [
      ['magic', ['style', 'h1', 'h2', 'h3', 'h4']],
        ['actions', ['undo', 'redo']],
        ['style', ['bold', 'italic', 'underline', 'clear']],
        ['font', ['fontname', 'strikethrough', 'superscript', 'subscript']],
        ['fontsize', ['fontsize']],
        ['color', ['color']],
        ['para', ['ul', 'ol', 'paragraph']],
        ['height', ['height']],
        ['media', [ 'link', 'table', 'hr']],
        ['insert', ['map', 'localmap']],
        ['uploadcare', ['uploadcare']],
        ['misc', ['help', 'fullscreen']]
    ],
    //disable: ["insertImage", "insertVideo"],
  });
  $(".summernote").each(function () {
    $(this).summernote({
      minHeight: 300,
      toolbar: [
        ['magic', ['style', 'h1', 'h2', 'h3', 'h4']],
        ['actions', ['undo', 'redo']],
        ['style', ['bold', 'italic', 'underline', 'clear']],
        ['font', ['fontname', 'strikethrough', 'superscript', 'subscript']],
        ['fontsize', ['fontsize']],
        ['color', ['color']],
        ['para', ['ul', 'ol', 'paragraph']],
        ['height', ['height']],
        ['media', ['picture', 'video', 'link', 'table', 'hr']],
        ['insert', ['map', 'localmap']],
        ['uploadcare', ['uploadcare']],
        ['misc', ['help', 'fullscreen']] 

      ],
      //disable: ["insertImage", "insertVideo"],
    });
  });
});
