import '/styles/bootstrap.min.css'
import '/styles/slick.css'
import '/styles/slick-theme.css'
import '/styles/base.css'
import '/styles/style.css'
import NavBar from '/components/comman/navbar'
import Footer from '/components/comman/footer'
import Script from 'next/script';
import Image from 'next/image'

function MyApp({ Component, pageProps }) {
  return(
    <div className='themebgcolor'>

      <Script type="text/javascript" strategy='afterInteractive' src="/js/jquery-2.0.0.min.js"/>
      {/* <Script type="text/javascript" strategy='lazyOnload' src="/js/bootstrap.bundle.min.js"/> */}
      <Script type="text/javascript" strategy='lazyOnload' src="/js/app.js"/>

      <div className="circlebg1"><Image width={525} height={548} className="img-fluid" src="/img/circlebg19.svg" alt="img"/></div>
      <div className="circlebg3"><Image width={714} height={719} className="img-fluid" src="/img/circlebg21.svg" alt="img"/></div>
      <NavBar/>
      <Component {...pageProps} />
      <Footer/>
    </div>
    )
}

export default MyApp
