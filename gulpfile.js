var gulp = require('gulp'),
    usemin = require('gulp-usemin'),
    del = require('del'),
    runSequence = require('run-sequence'),
    cssmin = require('gulp-css'),
    rev = require('gulp-rev'),
    rename = require('gulp-rename'),
    shell = require('gulp-shell'),
    argv = require('yargs').argv,
    sass = require('gulp-sass'),
    uglify = require('gulp-uglify'),
    minifyHtml = require('gulp-minify-html');

gulp.task('sass', function () {
    return gulp.src('./app/static/scss/**/*.scss')
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest('./app/static/scss'));
});

gulp.task('sass:watch', function () {
    gulp.watch('./app/static/scss/**/*.scss', ['sass']);
});

gulp.task("build:clean", function () {
    return del(["build"]);
})

gulp.task("build:dependencies", function () {
    return gulp.src(["requirements.txt"])
        .pipe(gulp.dest("build"))
})

gulp.task("build:backend", function () {
    return gulp.src(["**/*.py", "**/*.cfg", "!virtualenv/**/*", "!node_modules/**/*"])
        .pipe(gulp.dest("build"))
})

gulp.task("build:frontend", function () {
    return gulp.src('**/views/**/*.html')
        .pipe(usemin({
            assetsDir: "./app",
            path: ".",
            css: [cssmin(), rev(), rename({ dirname: 'app/static' })],
            js: [rev(), rename({ dirname: 'app/static' })],
            //html: [minifyHtml({ empty: true })],
            inlinejs: [uglify()]
        }))
        .pipe(gulp.dest('build'));
})

gulp.task("build", function (cb) {
    return runSequence("build:clean", "sass", ["build:backend", "build:dependencies", "build:frontend"], cb)
})

gulp.task("deploy", function (cb) {
    return runSequence("build", "push", cb)
})

gulp.task("push", shell.task([
    'echo hello' + argv["app"]
]));

