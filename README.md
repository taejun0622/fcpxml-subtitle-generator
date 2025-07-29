# FCPXML Subtitle Generator

[![PyPI version](https://badge.fury.io/py/fcpxml-subtitle-generator.svg)](https://badge.fury.io/py/fcpxml-subtitle-generator)
[![Python](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A powerful CLI tool to generate Final Cut Pro compatible subtitle files from audio/video files using OpenAI's Whisper AI transcription.

## 🚀 Features

- **Multiple file format support**: MP3, MP4, WAV, M4A
- **Automatic audio extraction**: Extracts audio from MP4 video files
- **AI-powered transcription**: Uses OpenAI Whisper for accurate speech-to-text
- **Final Cut Pro integration**: Generates FCPXML subtitle files compatible with Final Cut Pro
- **Multiple model sizes**: Choose from tiny, base, small, medium, or large Whisper models for speed/quality balance
- **Multi-language support**: Auto-detect or specify language for better accuracy
- **Frame-accurate timing**: Generates subtitles with precise frame boundaries (30fps)
- **Easy installation**: Available on PyPI with simple pip install

## 📦 Installation

Install from PyPI with a single command:

```bash
pip install fcpxml-subtitle-generator
```

**Requirements:**
- Python 3.13 or higher
- FFmpeg (for video processing)

## 🎯 Quick Start

### Basic Usage

Generate subtitles from an audio file:
```bash
fs-gen input.mp3
```

Generate subtitles from a video file (audio will be extracted automatically):
```bash
fs-gen input.mp4
```

### Advanced Usage

```bash
# Specify output file
fs-gen input.mp3 -o custom_subtitles.fcpxml

# Use a different Whisper model (higher quality but slower)
fs-gen input.mp3 -m large

# Specify language for better accuracy
fs-gen input.mp3 -l en

# Combine all options
fs-gen input.mp4 -o subtitles.fcpxml -m medium -l ko
```

## 📋 Command Line Arguments

| Argument | Short | Description | Default |
|----------|--------|-------------|---------|
| `input_file` | - | Path to input audio/video file | Required |
| `--output` | `-o` | Output FCPXML file path | `input_filename.fcpxml` |
| `--model` | `-m` | Whisper model size | `base` |
| `--language` | `-l` | Language code (e.g., 'en', 'ko', 'ja') | Auto-detect |
| `--help` | `-h` | Show help message | - |

### Whisper Model Sizes

| Model | Speed | Quality | Use Case |
|-------|-------|---------|----------|
| `tiny` | Fastest | Lowest | Quick drafts |
| `base` | Fast | Good | **Default - balanced** |
| `small` | Medium | Better | Higher quality |
| `medium` | Slow | High | Professional use |
| `large` | Slowest | Highest | Maximum accuracy |

### Supported Languages

Common language codes:
- `en` - English
- `ko` - Korean
- `ja` - Japanese
- `zh` - Chinese
- `es` - Spanish
- `fr` - French
- `de` - German
- `it` - Italian
- `pt` - Portuguese
- `ru` - Russian

*Auto-detection is used when no language is specified.*

## 🎬 Output Format

The tool generates FCPXML files that can be directly imported into Final Cut Pro as subtitle tracks:

- **Format**: FCPXML 1.11 standard
- **Frame Rate**: 30fps (1001/30000s per frame)
- **Text Encoding**: UTF-8 with XML escaping
- **Timing**: Frame-accurate subtitle positioning
- **Effect**: Uses Basic Title effect for Final Cut Pro compatibility

## 💡 Usage Examples

### Process a Podcast
```bash
fs-gen podcast.mp3
# Output: podcast.fcpxml
```

### Video Interview with Korean Language
```bash
fs-gen interview.mp4 -l ko -m medium
# Output: interview.fcpxml
```

### High-Quality Transcription for Presentation
```bash
fs-gen presentation.mp4 -m large -o presentation_subs.fcpxml
# Output: presentation_subs.fcpxml
```

### Batch Processing (Shell)
```bash
# Process all MP4 files in current directory
for file in *.mp4; do
    fs-gen "$file" -m base -l en
done
```

## 🔧 Technical Details

- **Audio Processing**: Temporary WAV files for MP4 audio extraction
- **AI Model**: OpenAI Whisper with word-level timestamps
- **Frame Synchronization**: Rounds to nearest 30fps frame boundary
- **Memory Usage**: Optimized for large files with temporary file cleanup
- **Error Handling**: Comprehensive error messages and graceful failures

## 🛠️ Development

### Local Development Setup

```bash
# Clone the repository
git clone https://github.com/taejun0622/fcpxml-subtitle-generator.git
cd fcpxml-subtitle-generator

# Install in development mode
pip install -e .

# Run from source
python subtitle_generator.py input.mp3
```

### Building from Source

```bash
# Install build tools
pip install build twine

# Build the package
python -m build

# The built files will be in dist/
```

## 🐛 Troubleshooting

### Common Issues

**FFmpeg not found:**
```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt install ffmpeg

# Windows
# Download from https://ffmpeg.org/download.html
```

**Out of memory error:**
```bash
# Use a smaller model
fs-gen input.mp4 -m tiny
```

**Wrong language detected:**
```bash
# Specify the language explicitly
fs-gen input.mp3 -l ko
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

- **PyPI Package**: https://pypi.org/project/fcpxml-subtitle-generator/
- **Issues**: Please report bugs and feature requests via GitHub issues
- **Documentation**: This README contains comprehensive usage information

## 🙏 Acknowledgments

- [OpenAI Whisper](https://github.com/openai/whisper) for the amazing speech recognition
- [MoviePy](https://github.com/Zulko/moviepy) for video/audio processing
- The Python packaging community for excellent tools and documentation

---

**Made with ❤️ for video editors and content creators**