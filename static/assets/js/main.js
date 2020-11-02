'use strict';


(function($) {
	/*------------------
		Navigation
	--------------------*/
	$(".main-menu").slicknav({
        appendTo: '.header-section',
		allowParentLinks: true,
		closedSymbol: '<i class="fa fa-angle-right"></i>',
		openedSymbol: '<i class="fa fa-angle-down"></i>'
	});
	
	$('.slicknav_nav').prepend('<li class="header-right-warp"></li>');
    $('.header-right').clone().prependTo('.slicknav_nav > .header-right-warp');

	/*------------------
		Background Set
	--------------------*/
	$('.set-bg').each(function() {
		var bg = $(this).data('setbg');
		$(this).css('background-image', 'url(' + bg + ')');
	});

	
	$('.hero-slider').owlCarousel({
		loop: true,
		nav: false,
		dots: true,
		mouseDrag: false,
		animateOut: 'fadeOut',
		animateIn: 'fadeIn',
		items: 1,
		autoplay: true
	});

	// feature detection for drag&drop upload

	var isAdvancedUpload = function()
	{
		var div = document.createElement( 'div' );
		return ( ( 'draggable' in div ) || ( 'ondragstart' in div && 'ondrop' in div ) ) && 'FormData' in window && 'FileReader' in window;
	}();


// applying the effect for every form

$( '.box' ).each( function()
{
	var $form		 = $( this ),
		$input		 = $form.find( 'input[type="file"]' ),
		$label		 = $form.find( 'label' ),
		$errorMsg	 = $form.find( '.box-error span' ),
		$restart	 = $form.find( '.box-restart' ),
		droppedFiles = false,
		showFiles	 = function( files )
		{
			$label.text( files.length > 1 ? ( $input.attr( 'data-multiple-caption' ) || '' ).replace( '{count}', files.length ) : files[ 0 ].name );
		};

	// letting the server side to know we are going to make an Ajax request
	$form.append( '<input type="hidden" name="ajax" value="1" />' );

	// automatically submit the form on file select
	$input.on( 'change', function( e )
	{
		showFiles( e.target.files );

		
	});


	// drag&drop files if the feature is available
	if( isAdvancedUpload )
	{
		$form
		.addClass( 'has-advanced-upload' ) // letting the CSS part to know drag&drop is supported by the browser
		.on( 'drag dragstart dragend dragover dragenter dragleave drop', function( e )
		{
			// preventing the unwanted behaviours
			e.preventDefault();
			e.stopPropagation();
		})
		.on( 'dragover dragenter', function() //
		{
			$form.addClass( 'is-dragover' );
		})
		.on( 'dragleave dragend drop', function()
		{
			$form.removeClass( 'is-dragover' );
		})
		.on( 'drop', function( e )
		{
			droppedFiles = e.originalEvent.dataTransfer.files; // the files that were dropped
			showFiles( droppedFiles );

			
		});
	}})

})(jQuery);


  