<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<br />
<div align="center">
<h3 align="center">comfy-magick</h3>

  <p align="center">
    A rough implementation of various ImageMagick functionalities in ComfyUI.
    <!-- <br />
    <a href="https://github.com/houdinii/comfy-magick"><strong>Explore the docs »</strong></a> -->
    <br />
    <br />
    <!-- <a href="https://github.com/houdinii/comfy-magick">View Demo</a>
    · -->
    <a href="https://github.com/houdinii/comfy-magick/issues">Report Bug</a>
    ·
    <a href="https://github.com/houdinii/comfy-magick/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is a way to implement ImageMagick functionality in ComfyUI, which is generally PIL (pillow) based. I'm not sure the
best way to handle this, as batch images make it a lot more complex, but the general idea will be two nodes to translate
the IMAGE type, a torch.tensor of shape [batch, width, height, channels], or [1, 600,  800, 3] for a single 800x600 image,
into/from a wand Image object. 

The nodes in between will not be compatible with other nodes until it is translated back into tensor form. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

The way to install this is the same as other custom nodes. Navigate to ComfyUI and clone this repo using the command:

`git clone https://github.com/houdinii/comfy-magick.git`

Restart the ComfyUI server.

### Prerequisites

Right now, this is using wand version 0.6.13 which uses ImageMagick bindings for version 7.

This does require ImageMagick to be on the PATH (for Windows). I'm not entirely sure how this would be set up on other
OSes, however there are instructions in the wand documentation found at: https://docs.wand-py.org/en/0.6.12/guide/install.html

<!--
### Installation

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/houdinii/comfy-magick.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>
-->


<!-- ROADMAP -->
## Roadmap

- [ ] Licenses / Readme
- [ ] First set of nodes, like CropByAspectRatio to get the ball rolling
- [ ] Adding features to this list
    - [ ] And more here....

See the [open issues](https://github.com/houdinii/comfy-magick/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License (For now. I want permissive licensing). See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Houdinii - [@harry-houdinii](https://twitter.com/harry-houdinii)

Project Link: [https://github.com/houdinii/comfy-magick](https://github.com/houdinii/comfy-magick)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [ImageMagick]()
* [wand]()
* [EllangoK/ComfyUI-post-processing-nodes]()
* [othneildrew/Best-README-Template]()

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/houdinii/comfy-magick.svg?style=for-the-badge
[contributors-url]: https://github.com/houdinii/comfy-magick/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/houdinii/comfy-magick.svg?style=for-the-badge
[forks-url]: https://github.com/houdinii/comfy-magick/network/members
[stars-shield]: https://img.shields.io/github/stars/houdinii/comfy-magick.svg?style=for-the-badge
[stars-url]: https://github.com/houdinii/comfy-magick/stargazers
[issues-shield]: https://img.shields.io/github/issues/houdinii/comfy-magick.svg?style=for-the-badge
[issues-url]: https://github.com/houdinii/comfy-magick/issues
[license-shield]: https://img.shields.io/github/license/houdinii/comfy-magick.svg?style=for-the-badge
[license-url]: https://github.com/houdinii/comfy-magick/blob/master/LICENSE.txt
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 




----------------------

ImageMagick is Apache 2.0 license
https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwilo46Ll-OEAxX4ENAFHYeABc8QFnoECAcQAQ&url=https%3A%2F%2Fimagemagick.org%2Fscript%2Flicense.php&usg=AOvVaw0MLxNNicF-KnYPZozkNf2g&opi=89978449

wand is license
custom license included

some functionality for loading into PIL form is from another package, EllangoK/ComfyUI-post-processing-nodes
I don't know the license offhand, but I think it's MIT 3.0. Double check.

Readme template from: othneildrew/Best-README-Template under MIT 3.0

I don't know what license to use, but it's going to be very permissive 

Todo:
- Licenses
- This Readme
